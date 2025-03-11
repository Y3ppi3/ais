# app/routers/products.py
from fastapi import APIRouter


router = APIRouter()

@router.get("/")
def get_products():
    return {"message": "Список продуктов"}
