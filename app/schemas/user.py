from pydantic import BaseModel, validator

permissions = ("админ", "продавец", "пользователь")

class User(BaseModel):
    id: int
    login: str
    password: str
    permssion: str
    
    
    @validator('password')
    def password_validator(cls, password):
        if len(password) < 8:
            raise ValueError('password length less than 8')
        return password


    @validator('permission')
    def password_validator(cls, value):
        if value not in permissions:
            raise ValueError('make coorect permissions')
        return value
