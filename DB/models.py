from pydantic import BaseModel, Field
from typing import List,Dict
from datetime import datetime

class Category(BaseModel):
    category_name: str

class Menu(BaseModel):
    menu_name: str
    menu_image: str
    menu_description: str
    menu_price: int

class OrderDetail(BaseModel):
    order_menu_id: str
    order_menu_name: str
    order_menu_amount: int
    order_menu_price: int

class Order(BaseModel):
    #order_number: str
    order_takeout: bool
    order_date: str = ""
    order_details: List[OrderDetail]
    total_amount: int = 0 
    total_price: int = 0

    def __init__(self, **data):
        super().__init__(**data)
        self.order_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.total_amount = sum(order.order_menu_amount for order in self.order_details)
        self.total_price = sum(order.order_menu_price for order in self.order_details)



    