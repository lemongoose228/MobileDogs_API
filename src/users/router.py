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

@router.post("/user/registr", response_model=schemas.ResponseUser)
async def UserRegistration(user: schemas.CreateUser, db: DBSession = Depends(session)):
    if crud.find_user(db, user.login):
        raise exceptions.BusyLogin()
    new_user = crud.create_user(db, user)
    result = schemas.ResponseUser(success=True, accessToken=new_user.accessToken)
    return result

@router.post("/user/login", response_model=schemas.ResponseUserLogin)
async def UserLogin(user: schemas.LoginUser, db: DBSession = Depends(session)):

    if not crud.find_user(db, user.login):
        raise exceptions.WrongLogin()
    if not crud.check_password(db, user.login, user.password):
        raise exceptions.WrongPassword()
    if not crud.check_token(db, user.login, user.accessToken):
        raise exceptions.WrongToken()

    result = schemas.ResponseUserLogin(success=True, message="Вы успешно вошли в аккаунт")
    return result

@router.post("/user/creatTask", response_model=schemas.CreateTaskResponse)
async def UserCreateTask(task: schemas.CreateTask, db: DBSession = Depends(session)):
    if not crud1.find_collar(db, task.collar_id):
        raise exceptions1.NotExistCollar()
    if not crud.find_token(db, task.accessToken):
        raise exceptions.WrongToken()

    task_from_db = crud.create_task(db, task)

    result = schemas.CreateTaskResponse(task_id=task_from_db.id, success=True, message="Вы успешно создали задание")
    return result

@router.post("/user/showDogsTasks", response_model=schemas.showDogsTasksResponse)
async def showDogsTasks(task: schemas.showDogsTasks, db: DBSession = Depends(session)):
    if not crud1.find_collar(db, task.collar_id):
        raise exceptions1.NotExistCollar()

    task_from_db = crud.get_tasks(db, task.collar_id)

    result = schemas.showDogsTasksResponse(tasks=task_from_db)
    return result

@router.post("/user/subscribe", response_model=schemas.ResponseSubscribtion)
async def SudscrCreate(subscr: schemas.CreateSubscribtion, db: DBSession = Depends(session)):
    if not crud1.find_collar(db, subscr.collar_id):
        raise exceptions.DogDoesntExist()
    if not crud.find_user(db, subscr.user_login):
        raise exceptions.UserDoesntExist()
    if crud.find_subscr(db, subscr.user_login, subscr.collar_id):
        raise exceptions.ExistSubscr()
    
    new_subscr = crud.create_subscr(db, subscr)
    result = schemas.ResponseSubscribtion(success=True, accessToken=new_subscr.accessToken)
    return result
