from fastapi import FastAPI 

from config.db import init_db 
import logging

log = logging.getLogger(__name__)


def create_application() -> FastAPI:
    application = FastAPI(
        title="IndoAnalytics"
    )

    return application


app = create_application()

@app.on_event("startup")
async def startup_event():
    print("Starting up...")
    init_db(app)


@app.on_event("shutdown")
async def shutdown_event():
    print("Shutting down...")


@app.get('/')
def index():
    return {
        'index': 'welcome'
    }

from models.models import UserInSchema, UserSchema, Users

@app.post('/users', response_model=UserSchema)
async def create_user(user: UserInSchema):
    user_obj = await Users.create(**user.dict(exclude_unset=True))
    return await UserSchema.from_tortoise_orm(user_obj)

from typing import List


@app.get("/users", response_model=List[UserSchema])
async def get_users():
    return await UserSchema.from_queryset(Users.all())

