from fastapi import HTTPException, status

class BusyCollar(HTTPException):
    def __init__(self):
        super().__init__(status_code=status.HTTP_400_BAD_REQUEST, detail="Этот ошейник занят")

class NotExistCollar(HTTPException):
    def __init__(self):
        super().__init__(status_code=status.HTTP_400_BAD_REQUEST, detail="Собака с таким ошейником не зарегистрирована")
