from DB.db import category_collection, menu_collection
from DB.models import Category, Menu
from bson import ObjectId

class CategoryService:
    def create_category(self, category: Category):
        category_collection.insert_one(dict(category))

    def fetch_category(self, id: str):
        category = category_collection.find_one({"_id": ObjectId(id)})
        if category:
            return {
                "id": str(category['_id']),
                "category_name": category.get('category_name', '')
            }
        return None
    
    def fetch_categories(self) -> list:
        categories = category_collection.find()
        return [self.fetch_category(category) for category in categories]
    
class MenuService:
    def create_menu(self, menu: Menu):
        menu_collection.insert_one(dict(menu))

    def fetch_menu(self, id: str):
        menu = menu_collection.find_one({"_id": ObjectId(id)})
        if menu:
            return {
                "id": str(menu['_id']), 
                "menu_name": menu.get('menu_name', ''),
                "menu_image": menu.get('menu_image', ''),
                "menu_description": menu.get('menu_description', ''),
                "menu_price": menu.get('menu_price', 0),
            }
        return None

    def fetch_menus(self) -> list:
        menus = menu_collection.find()
        return [self.fetch_menu(menu["_id"]) for menu in menus]
    
    def delete_menu(self, id: str):
        menu_collection.delete_one({"_id": ObjectId(id)})

    def update_menu(self, id: str, menu: Menu):
        menu = menu_collection.update_one({"_id": ObjectId(id)}, {"$set": dict(menu)})

