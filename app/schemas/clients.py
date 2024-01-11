from pydantic import BaseModel,  validator

class Clients(BaseModel):
    id: int
    client_name: str
    client_surname: str
    client_phone: str
    client_addres: str

    @validator("client_phone")
    @classmethod
    def validate_phone(cls,value):
        numbers = list(map(str,value.split("-")))
        if len(numbers) != 3:
            raise ValueError("Phone Number is uncorrect")
        elif len(numbers[0]) != 3 or  len(numbers[1]) != 3 or  len(numbers[2]) != 4:
            raise ValueError("Phone Number is uncorrect")
        else:
            return value
