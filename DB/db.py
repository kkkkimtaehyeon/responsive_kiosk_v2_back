from pymongo import MongoClient
import os
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())
MONGODB_URL = os.getenv('MONGODB_URL')
client = MongoClient(MONGODB_URL)

db = client.kiosk

category_collection = db['category']
menu_collection = db['menu']
order_collection = db['order'] # 컬렉션이 없다면 자동으로 생성