from pydantic import BaseModel

class Orders(BaseModel):
    id: int
    product_id: int
    order_id: int