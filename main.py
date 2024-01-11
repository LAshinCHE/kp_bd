from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates 
from app.dataBase.db import *
import psycopg2
from app.routers import orders, product, clients, order_products, category,user
from fastapi.responses import HTMLResponse
from app.dataBase.db import get_connection


app = FastAPI(
    title="Order_shop"
)

templates = Jinja2Templates(directory="./app/template")

app.include_router(orders.router)
app.include_router(product.router)
app.include_router(clients.router)
app.include_router(order_products.router)
app.include_router(category.router)
app.include_router(user.router)


@app.get("/main/")
async def print_hello(request: Request):
    response = check_version()
    return templates.TemplateResponse("main_page.html", {"status": 200, "request": request, "data": response})

@app.get("/")
async def select_your_permission(request: Request):
    return templates.TemplateResponse("start_page.html", {"status": 200, "request": request})

@app.get("/main/{user_id}")
async def main_user_page(request: Request, user_id: int):
    conn, cur = get_connection()
    req = cur.mogrify("""SELECT user_permission FROM users""")
    cur.execute(req)
    data = cur.fetchall()
    if data[0][0] == "пользователь":
        data_push = user_id
        return templates.TemplateResponse("user_page.html", {"status": 200, "request": request, "data": data_push})
    if data[0][0] == "продавец":
        data_push = user_id
        return templates.TemplateResponse("main_page.html", {"status": 200, "request": request, "data": data_push})
    conn.commit()  
    return templates.TemplateResponse("main_page.html", {"status": 200, "request": request})

# Handle form submission
