from fastapi import APIRouter, Form
from fastapi import Request
from typing import Union
from fastapi.responses import HTMLResponse
from app.schemas.clients import Clients
from app.dataBase.clients import *
from fastapi.templating import Jinja2Templates

router = APIRouter(
    prefix="/clients",
    tags=["clients"]
)

templates = Jinja2Templates(directory="./app/template")


@router.post("/")
def add_new_client(client: List[Clients]):
    response = post_client(client)
    return {"status": 200, "data": response}



@router.get("/", response_class=HTMLResponse)
async def  get_clients(request: Request):
    response = get_clients_db()
    return templates.TemplateResponse("clients_page.html", {"status": 200,"request": request, "data": response})



@router.get("/{user_id}", response_model=Clients)
async def  get_clients(request: Request, user_id : int):
    response = get_client(user_id)
    return templates.TemplateResponse("clients_page.html", {"status": 200,"request": request, "data": response})


@router.post("/{user_id}", response_class=HTMLResponse)
async def edit_client(
    request: Request,
    user_id: int,
    username: str = Form(...),
    surname: str = Form(...),
    phone: str = Form(...),
    address: str = Form(...),
): 
    try:
        change_client(
            Clients(
                id=user_id,
                client_name=username,
                client_surname=surname,
                client_phone=phone,
                client_addres=address,
            )
        )
    except ValueError  as exc:
        print("LOG: POST REQUEST IS WORCK")
        return templates.TemplateResponse("exception_page.html", {"status": 200, "request": request, "data": exc})
    response = get_client(user_id)
    return templates.TemplateResponse("clients_page.html", {"status": 200,"request": request, "data": response})
    
