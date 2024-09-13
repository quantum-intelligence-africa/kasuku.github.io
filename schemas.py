from pydantic import BaseModel

class UserCreate(BaseModel):
    email: str

    class Config:
        orm_mode = True
