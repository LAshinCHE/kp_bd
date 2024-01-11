from fastapi import APIRouter, Form
from fastapi import Request
from fastapi.responses import HTMLResponse
from app.dataBase.orders import *
from app.dataBase.order_products import make_order_and_products
from app.schemas.orders import Orders
from fastapi.templating import Jinja2Templates
from fastapi.exceptions import RequestValidationError
from pydantic import BaseModel, ValidationError, field_validator
from datetime import datetime

router = APIRouter(
    prefix="/orders",
    tags=["orders"]
)

templates = Jinja2Templates(directory="./app/template")

@router.get("/", response_class=HTMLResponse)
async def get_orders(request: Request):
    result = get_orders_db()
    return templates.TemplateResponse("orders_page.html", {"status": 200,"request": request, "data": result})

@router.get("/{user_id}", response_class=HTMLResponse)
async def get_orders(request: Request, user_id : int):
    result = get_user_orders(user_id)
    if len(result):
        return templates.TemplateResponse("orders_page.html", {"status": 200,"request": request, "data": result, "user_id": user_id})
    else:
        return templates.TemplateResponse("404.html", {"status": 404,"request": request})


@router.post("/{user_id}/{product_id}", response_class=HTMLResponse)
async def add_order(
    request: Request,
    user_id: int,
    product_id: int,
):
    order_status_val ='Ожидается'
    order_id_val = take_max_id()[0][0] + 1
    order_number_val = "ORD"+str(order_id_val)
    order_date_val = datetime.now()
    order_delivery_val = False
    order_client_id_val  = user_id
    print("order_id: " + str(order_id_val) )
    print("order_numbers: " +  order_number_val)
    print("order data: " + str(order_date_val))
    print("oreder_delivery: " + str(order_delivery_val))
    print("order_client_id: " +  str(order_client_id_val))

    
    make_order(Orders(
        id=order_id_val,
        order_number=order_number_val,
        order_date=order_date_val,
        order_status=order_status_val,
        order_delivery=order_delivery_val,
        client_id=order_client_id_val
    ))
    make_order_and_products(product_id, order_id_val)
    response = get_user_orders(user_id)
    return templates.TemplateResponse("orders_page.html", {"status": 200,"request": request, "data": response})
    

@router.delete("/{user_id}/{order_id}",response_class=HTMLResponse)
def delete_order(request: Request,
                 user_id: int,
                 order_id: int,
                ):
    print("LOG: DELETE REQUEST")
    delete_order_db(order_id)
    response = get_user_orders(user_id)
    return templates.TemplateResponse("orders_page.html", {"status": 200,"request": request, "data": response})
    
    