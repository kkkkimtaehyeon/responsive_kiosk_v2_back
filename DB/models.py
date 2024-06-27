from pydantic import BaseModel

class Category(BaseModel):
    category_name: str

class Menu(BaseModel):
    menu_name: str
    menu_image: str
    menu_description: str
    menu_price: int