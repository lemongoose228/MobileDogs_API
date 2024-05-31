import devices.crud as crud
import devices.schemas as schemas
import devices.exceptions as exceptions
import users.crud as crud1
import users.exceptions as exceptions1
from dependecies import session
from database import DBSession
from fastapi import APIRouter, Depends

router = APIRouter()

@router.post("/dogs/registr", response_model=schemas.ResponseDog)
async def DogsRegistration(dog: schemas.CreateDog, db: DBSession = Depends(session)):
    if crud.find_collar(db, dog.collar_id):
        raise exceptions.BusyCollar()
    new_dog = crud.create_collar(db, dog)
    result = schemas.ResponseDog(success=True, collar_token=new_dog.collar_token)
    return result

@router.post("/user/getDogsSubscribers", response_model=schemas.GetDogsSubscribersResponse)
async def dog_subscriptions(data_for_subs: schemas.GetDogsSubscribers, db: DBSession = Depends(session)):
    if not crud.find_collar(db, data_for_subs.collar_id):
        raise exceptions1.DogDoesntExist()

    subs_from_db = crud.get_dog_subscr(db, data_for_subs.collar_id)

    result = schemas.GetDogsSubscribersResponse(subs=subs_from_db)
    return result

@router.post("/dogs/getDogsGeoPos", response_model=schemas.GetDogsPosResponse)
async def dog_subscriptions(collar_id: schemas.GetDogsPos, db: DBSession = Depends(session)):
    if not crud.find_collar(db, collar_id.collar_id):
        raise exceptions1.DogDoesntExist()

    pos = crud.generate_coordinates(collar_id.collar_id)

    return {"latitude": pos[0],
            "longitude": pos[1],}
