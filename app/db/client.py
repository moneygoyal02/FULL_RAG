from pymongo import AsyncMongoClient
from dotenv import load_dotenv
import os

load_dotenv()
MONGODB_URI = os.getenv("MONGODB_URI")
mongo_client: AsyncMongoClient = AsyncMongoClient(MONGODB_URI)
