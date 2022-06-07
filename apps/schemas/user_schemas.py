from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    email: str


class UserSchema(UserBase):
    first_name: str
    last_name: str

    class Config:
        orm_mode = True


class UserCreateSchema(UserSchema):
    password: str
    username: str

    class Config:
        orm_mode = False 
