
from typing import List
from pydantic import BaseModel

class ItemBase(BaseModel):
    title: str
    description: str | None = None


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True






class UserBase(BaseModel):
    email: str


class UserCreate(UserBase): # When you create a user, they need to register with an email and passowrd
    password: str



class User(UserBase): # If youre storing or returning a user in your DB, You don't want to store their password
    id: int
    is_active: bool
    items: list[Item] = []

    class Config: 
        orm_mode = True # Will try to read the data, possibly as a dict, possibly not. # It will eagerly fetch data in a relationship setup.



