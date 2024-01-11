from pydantic import BaseModel

class Categories(BaseModel):
    id: int
    categoty_name: str

