from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    MONGODB_URI = os.getenv("MONGODB_URI")
    SECRET_KEY = os.getenv("SECRET_KEY")
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
    JWT_ACCESS_TOKEN_EXPIRES = int(os.getenv("JWT_ACCESS_TOKEN_EXPIRES", 30))
