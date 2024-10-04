from pydantic import BaseModel

class UserSchema(BaseModel):
    name:str
    password:str

class GetFromName(BaseModel):
    name:str