from pydantic import BaseModel


class UserSchema(BaseModel):
    id: int
    name: str


class CarSchema(BaseModel):
    id: int
    name: str


class OrderSchema(BaseModel):
    user_id: int
    car_id: int


class GetName(BaseModel):
    name: str


class GetId(BaseModel):
    id: int
