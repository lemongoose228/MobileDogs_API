from fastapi import FastAPI
import uvicorn
from database import BaseDBModel, engine
from users.router import router
from devices.router import router as router1

BaseDBModel.metadata.create_all(bind=engine)
app = FastAPI()
app.include_router(router)
app.include_router(router1)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8002)

@app.get("/")
async def root():
    return {"message": "всё работает"}
