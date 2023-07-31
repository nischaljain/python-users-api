from pydantic import BaseModel


class UserBase(BaseModel):
    first_name: str 
    last_name: str
    age: int
    gender: str
    email: str
    phone: int
    birth_date: str


class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int

    class Config:
        orm_mode = True


