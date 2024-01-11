from fastapi import APIRouter
from fastapi import Request
from fastapi.responses import HTMLResponse
from app.dataBase.category import *
from fastapi.templating import Jinja2Templates

router = APIRouter(
    prefix="/category",
    tags=["category"]
)

templates = Jinja2Templates(directory="./app/template")



@router.get("/", response_class=HTMLResponse)
async def get_category(request: Request):
    result = get_category_db()
    return templates.TemplateResponse("category_page.html", {"status": 200,"request": request, "data": result})