from pydantic import BaseModel


class Products(BaseModel):
    id: int
    product_name: str
    product_price: int
    product_description: str
    category_id: int
    product_manufacturer: int
