from pydantic import BaseModel

class CreateUser(BaseModel):
    login: str
    password: str

class ResponseUser(BaseModel):
    success: bool
    accessToken: str

class LoginUser(BaseModel):
    login: str
    password: str
    accessToken: str

class ResponseUserLogin(BaseModel):
    success: bool
    message: str

class CreateTask(BaseModel):
    accessToken: str
    collar_id: int
    task: str

class CreateTaskResponse(BaseModel):
    task_id: int
    success: bool
    message: str

class showDogsTasks(BaseModel):
    collar_id: int

class showDogsTasksResponse(BaseModel):
    tasks: object

class CreateSubscribtion(BaseModel):
    user_login: str
    collar_id: str
    accessToken: str

class ResponseSubscribtion(BaseModel):
    success: bool
    accessToken: str

class DeleteSubscribtion(BaseModel):
    user_login: str
    collar_id: str
    accessToken: str

class ResponseDeleteSubscribtion(BaseModel):
    success: bool
    accessToken: str
