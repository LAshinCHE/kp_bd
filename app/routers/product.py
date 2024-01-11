from fastapi import APIRouter
from fastapi import Request
from fastapi.responses import HTMLResponse
from app.dataBase.product import *
from fastapi.templating import Jinja2Templates


router = APIRouter(
    prefix="/products",
    tags=["products"]
)

templates = Jinja2Templates(directory="./app/template")

@router.get("/", response_class=HTMLResponse)
async def get_orders(request: Request):
    result = get_products_db()
    return templates.TemplateResponse("products_page.html", {"status": 200,"request": request, "data": result})

@router.get("/{user_id}", response_class=HTMLResponse)
async def get_orders(request: Request, user_id : int):
    result = get_products_db()
    return templates.TemplateResponse("products_page.html", {"status": 200,"request": request, "data": result, "user_id": user_id})


