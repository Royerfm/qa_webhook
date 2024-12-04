import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_TOKEN = os.getenv("WEBHOOK_SECRET", "default_secret")
    DEBUG = os.getenv("FLASK_ENV") == "development"
