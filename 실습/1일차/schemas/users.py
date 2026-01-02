# app/schemas/users.py

from enum import Enum

from pydantic import BaseModel, conint


class GenderEnum(str, Enum):
    male = 'male'
    female = 'female'


class UserCreateRequest(BaseModel):
    username: str
    age: int
    gender: GenderEnum

    # app/schemas/users.py


class UserUpdateRequest(BaseModel):
    username: str | None = None
    age: int | None = None

# app/schemas/users.py



class UserSearchParams(BaseModel):
    model_config = {"extra": "forbid"}
    
    username: str | None = None
    age: conint(gt=0) | None = None
    gender: GenderEnum | None = None

    