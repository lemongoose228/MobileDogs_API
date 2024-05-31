from pydantic import BaseModel

class Dog(BaseModel):
    name: str

class CreateDog(Dog):
    collar_id: str

class ResponseDog(BaseModel):
    success: bool
    collar_token: str

class GetDogsSubscribers(BaseModel):
    collar_id: str

class GetDogsSubscribersResponse(BaseModel):
    subs: object

class GetDogsPos(BaseModel):
    collar_id: str

class GetDogsPosResponse(BaseModel):
    latitude: float
    longitude: float
