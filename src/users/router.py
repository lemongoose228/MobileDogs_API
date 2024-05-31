import users.crud as crud
import users.schemas as schemas
import users.exceptions as exceptions
from dependecies import session
from database import DBSession
import devices.exceptions as exceptions1
import devices.schemas as schemas1
import devices.crud as crud1
import devices.exceptions as exceptions1

from fastapi import APIRouter, Depends

router = APIRouter()

import logging, sys
from logging.handlers import TimedRotatingFileHandler
import platform

FORMATTER_STRING = f"%(asctime)s — %(name)s — %(levelname)s — %(message)s - {platform.platform()}"
FORMATTER = logging.Formatter(FORMATTER_STRING)
LOG_FILE = "tmp/user_loggs.log"

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

logger = get_logger('user_logger')

@router.post("/user/registr", response_model=schemas.ResponseUser)
async def UserRegistration(user: schemas.CreateUser, db: DBSession = Depends(session)):
    if crud.find_user(db, user.login):
        logger.warning(f'Не удалось создать пользователя! Пользователь c логином {user.login} уже существует')
        raise exceptions.BusyLogin()
    new_user = crud.create_user(db, user)
    result = schemas.ResponseUser(success=True, accessToken=new_user.accessToken)

    logger.info(f'Пользователь {user.login} успешно зарегистрирован')
    return result

@router.post("/user/login", response_model=schemas.ResponseUserLogin)
async def UserLogin(user: schemas.LoginUser, db: DBSession = Depends(session)):

    if not crud.find_user(db, user.login):
        logger.warning(f'Не удалось войти в аккаунт! Пользователь c логином {user.login} не заргеистрирован')
        raise exceptions.WrongLogin()
    if not crud.check_password(db, user.login, user.password):
        logger.warning(f'Не удалось войти в аккаунт! Неправильный пароль')
        raise exceptions.WrongPassword()
    if not crud.check_tokenByLogin(db, user.login, user.accessToken):
        logger.warning(f'Не удалось войти в аккаунт! Неправильный токен')
        raise exceptions.WrongToken()

    result = schemas.ResponseUserLogin(success=True, message="Вы успешно вошли в аккаунт")
    logger.info(f'Пользователь {user.login} успешно вошёл в аккаунт')
    return result

@router.post("/user/creatTask", response_model=schemas.CreateTaskResponse)
async def UserCreateTask(task: schemas.CreateTask, db: DBSession = Depends(session)):
    if not crud1.find_collar(db, task.collar_id):
        logger.warning(f'Не удалось найти собаку с id ошейника {task.collar_id}')
        raise exceptions1.NotExistCollar()
    if not crud.find_token(db, task.accessToken):
        logger.warning(f'Не удалось найти пользователя с токеном {task.accessToken}')
        raise exceptions.WrongToken()

    task_from_db = crud.create_task(db, task)

    result = schemas.CreateTaskResponse(task_id=task_from_db.id, success=True, message="Вы успешно создали задание")
    logger.info(f'Задание c id {task_from_db.id} было успешно создано')
    return result

@router.post("/user/showDogsTasks", response_model=schemas.showDogsTasksResponse)
async def showDogsTasks(task: schemas.showDogsTasks, db: DBSession = Depends(session)):
    if not crud1.find_collar(db, task.collar_id):
        raise exceptions1.NotExistCollar()

    task_from_db = crud.get_tasks(db, task.collar_id)

    result = schemas.showDogsTasksResponse(tasks=task_from_db)
    return result

@router.post("/user/takeTask", response_model=schemas.takeTaskResponse)
async def takeTask(task: schemas.takeTask, db: DBSession = Depends(session)):
    if not crud.find_token(db, task.accessToken):
        raise exceptions.WrongToken()

    if not crud.check_taskId(db, task.task_id):
        raise exceptions.WrongnTaskId()

    crud.take_task(db, task)

    result = schemas.takeTaskResponse(success=True, message='Вы успшно взяли задание')
    return result


@router.post("/user/showUserTasks", response_model=schemas.showUserTasksResponse)
async def showDogsTasks(task: schemas.showUserTasks, db: DBSession = Depends(session)):
    if not crud.find_token(db, task.accessToken):
        raise exceptions.WrongToken()

    task_from_db = crud.get_user_tasks(db, task.accessToken)

    result = schemas.showUserTasksResponse(tasks=task_from_db)
    return result

@router.post("/user/becomeAdmin", response_model=schemas.becomeAdminResponse)
async def becomeAdmin(code: schemas.becomeAdmin, db: DBSession = Depends(session)):
    admin = crud.find_user(db, "admin")
    if crud.check_code(code.code):
        result = schemas.becomeAdminResponse(success=True, accessToken=admin.accessToken)
    else:
        raise exceptions.WrongCode()

    return result

@router.post("/user/subscribe", response_model=schemas.ResponseSubscribtion)
async def SudscrCreate(subscr: schemas.CreateSubscribtion, db: DBSession = Depends(session)):
    if not crud_dev.find_collar(db, subscr.collar_id):
        raise exceptions.DogDoesntExist()
    if not crud.find_user(db, subscr.user_login):
        raise exceptions.UserDoesntExist()
    if not crud.check_token(db, subscr.user_login, subscr.accessToken):
        raise exceptions.WrongToken()
    if crud.find_subscr(db, subscr.user_login, subscr.collar_id):
        raise exceptions.ExistSubscr()
    
    new_subscr = crud.create_subscr(db, subscr)
    result = schemas.ResponseSubscribtion(success=True, accessToken=new_subscr.accessToken)
    return result

@router.post("/user/unsubscribe", response_model=schemas.ResponseDeleteSubscribtion)
async def SudscrDelete(subscr: schemas.DeleteSubscribtion, db: DBSession = Depends(session)):
    if not crud1.find_collar(db, subscr.collar_id):
        raise exceptions.DogDoesntExist()
    if not crud.find_user(db, subscr.user_login):
        raise exceptions.UserDoesntExist()
    if not crud.check_token(db, subscr.user_login, subscr.accessToken):
        raise exceptions.WrongToken()
    if not crud.find_subscr(db, subscr.user_login, subscr.collar_id):
        raise exceptions.SubscrDoesntExist()

    deleted_subscr = crud.delete_subscr(db, subscr)
    if deleted_subscr:
        result = schemas.ResponseDeleteSubscribtion(success=True, message="Удаление выполнено успешно")
    return result

@router.post("/user/getUsersSubscribtions", response_model=schemas.GetUserSubscribtionResponse)
async def users_subscriptions(data_for_subs: schemas.GetUserSubscribtion, db: DBSession = Depends(session)):
    if not crud.find_user(db, data_for_subs.user_login):
        raise exceptions.UserDoesntExist()
    if not crud.check_token(db, data_for_subs.user_login, data_for_subs.accessToken):
        raise exceptions.WrongToken()

    subs_from_db = crud.get_user_subscr(db, data_for_subs.user_login, data_for_subs.accessToken)

    result = schemas.GetUserSubscribtionResponse(subs=subs_from_db)
    return result
