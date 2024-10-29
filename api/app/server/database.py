import pymongo
import os
from dotenv import load_dotenv

load_dotenv()

DB_URL = os.getenv('DB_URL')
client = pymongo.MongoClient(DB_URL)

db = client["Organisation"]
employeeCollection = db["employees"]
