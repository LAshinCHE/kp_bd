from fastapi import APIRouter, Form
from fastapi import Request
from fastapi.responses import RedirectResponse
from fastapi.responses import HTMLResponse
from app.dataBase.user import *
from fastapi.templating import Jinja2Templates
from fastapi.responses import JSONResponse, FileResponse


router = APIRouter(
    prefix="/user",
    tags=["user"]
)

templates = Jinja2Templates(directory="./app/template")

@router.post("/register/", response_class=HTMLResponse)
async def post_register(
    request: Request,
    username: str = Form(...),
    email: str = Form(...),
    password: str = Form(...),
):
    user = check_user(user_name=username, user_password=password)
    if user == None:
        responce = add_new_user(user_name=username,user_email=email, user_password=password)
    user_id = responce[0][0]
    return RedirectResponse(f"/main/{user_id}", status_code=302)

@router.get("/login/")
async def print_hello(request: Request):
    return templates.TemplateResponse("user_login_page.html", {"status": 200, "request": request})

@router.get("/register/")
async def print_hello(request: Request):
    return templates.TemplateResponse("registration_page.html", {"status": 200, "request": request})

@router.post("/login/", response_class=HTMLResponse)
async def post_register(
    request: Request,
    username: str = Form(...),
    password: str = Form(...),
):
    response = check_user(user_name=username, user_password=password)
    if len(response) != 0:
        response = get_user(user_name=username,user_password=password)
        user_id = response[0][0]
        return RedirectResponse(f"/main/{user_id}", status_code=302)
    else: 
        return RedirectResponse("/user/register/", status_code=302)
    