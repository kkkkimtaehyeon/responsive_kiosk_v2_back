from fastapi import APIRouter
from DB.schemas import CategoryService, MenuService, OrderService
from DB.models import Category, Menu, Order, OrderDetail
from typing import List

router = APIRouter(tags=['cafe'])

category_service = CategoryService()
menu_service = MenuService()
order_service = OrderService()

# 카테고리
@router.post("/categories")
async def create_category(category: Category):
    category_service.create_category(category)

@router.get("/categories")
async def fetch_categories():
    return category_service.fetch_categories()

# 메뉴
@router.post("/menus")
async def create_menu(menu: Menu):
    menu_service.create_menu(menu)

@router.get("/menus")
async def fetch_menus():
    return menu_service.fetch_menus()

@router.delete("/menus/{id}")
async def delete_menu(id: str):
    menu_service.delete_menu(id)

@router.patch("/menus/{id}")
async def update_menu(id: str, menu: Menu):
    menu_service.update_menu(id, menu)

# 주문
@router.post("/orders")
async def create_order(order: Order):
    #order_detail = [dict(order) for order in OrderDetail]
    return order_service.create_order(order)