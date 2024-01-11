from fastapi import APIRouter
from fastapi import Request
from fastapi.responses import HTMLResponse
from app.dataBase.order_products import *
from fastapi.templating import Jinja2Templates


router = APIRouter(
    prefix="/order_products",
    tags=["order_products"]
)

templates = Jinja2Templates(directory="./app/template")

@router.get("/", response_class=HTMLResponse)
async def get_order_product(request: Request):
    result = get_order_product_db()
    return templates.TemplateResponse("order_products.html", {"status": 200,"request": request, "data": result})
