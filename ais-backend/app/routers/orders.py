# app/routers/orders.py
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_orders():
    return {"message": "Список заказов"}
