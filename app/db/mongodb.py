from pymongo import MongoClient
from app.core.config import get_settings

settings = get_settings()

client = MongoClient(settings.MONGODB_BASE)
db = client[settings.MONGODB_DB]
