from pydantic import BaseModel, validator
from datetime import datetime


order_status_list = ("Ожидается", "Отправленный", "Доставленный")

class Orders(BaseModel):
    id: int
    order_number: str
    order_date: datetime | None
    order_status: str
    order_delivery: bool
    client_id: int

    @validator("order_status")
    @classmethod
    def validate_status(cls, value) :
        if value not in order_status_list:
            raise ValueError("Something wrong with your order status")
        return value

