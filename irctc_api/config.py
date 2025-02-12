import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://soham:soham123@localhost/irctc_db"
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "24dd80b83e54bfabd5e777ef97bb79fd35a51965cae12cfaebbdfdc00a390f94")
    ADMIN_API_KEY = os.getenv("ADMIN_API_KEY", "your_admin_api_key")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

