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
