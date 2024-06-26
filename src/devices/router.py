import devices.crud as crud
import devices.schemas as schemas
import devices.exceptions as exceptions
import users.crud as crud1
import users.exceptions as exceptions1
from dependecies import session
from database import DBSession
from fastapi import APIRouter, Depends

router = APIRouter()

import logging, sys
from logging.handlers import TimedRotatingFileHandler
import platform

FORMATTER_STRING = f"%(asctime)s — %(name)s — %(levelname)s — %(message)s - {platform.platform()}"
FORMATTER = logging.Formatter(FORMATTER_STRING)
LOG_FILE = "tmp/devices_loggs.log"

def get_logger(logger_name):
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.INFO)

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(FORMATTER)
    logger.addHandler(console_handler)

    file_handler = TimedRotatingFileHandler(LOG_FILE, when='midnight')
    file_handler.setFormatter(FORMATTER)
    logger.addHandler(file_handler)

    return logger

logger = get_logger('devices_logger')

@router.post("/dogs/registr", response_model=schemas.ResponseDog)
async def DogsRegistration(dog: schemas.CreateDog, db: DBSession = Depends(session)):
    if crud.find_collar(db, dog.collar_id):
        logger.error(f'Ошибка регистрации! Ошейник с id {dog.collar_id} уже зарегистрирован в системе')
        raise exceptions.BusyCollar()
    new_dog = crud.create_collar(db, dog)
    result = schemas.ResponseDog(success=True, collar_token=new_dog.collar_token)

    logger.info(f'Ошейник с id {dog.collar_id} успешно зарегистрирован')
    return result

@router.post("/user/getDogsSubscribers", response_model=schemas.GetDogsSubscribersResponse)
async def dog_subscriptions(data_for_subs: schemas.GetDogsSubscribers, db: DBSession = Depends(session)):
    if not crud.find_collar(db, data_for_subs.collar_id):
        logger.error(f'Ошейник с id {data_for_subs.collar_id} не зарегистрирован в системе')
        raise exceptions1.DogDoesntExist()

    subs_from_db = crud.get_dog_subscr(db, data_for_subs.collar_id)

    result = schemas.GetDogsSubscribersResponse(subs=subs_from_db)
    logger.info(f'Подписчики собаки с id {data_for_subs.collar_id} успешно выведены')
    return result

@router.post("/dogs/getDogsGeoPos", response_model=schemas.GetDogsPosResponse)
async def dog_subscriptions(collar_id: schemas.GetDogsPos, db: DBSession = Depends(session)):
    if not crud.find_collar(db, collar_id.collar_id):
        logger.error(f'Ошейник с id {collar_id.collar_id.collar_id} не зарегистрирован в системе')
        raise exceptions1.DogDoesntExist()

    pos = crud.generate_coordinates(collar_id.collar_id)
    logger.info(f'Гео позиция собаки выведена')
    return {"latitude": pos[0],
            "longitude": pos[1],}
