import os

class Settings:
    DATABASE_URL: str = os.getenv("DATABASE_URL", "mysql+mysqlconnector://root:testopenai123@mysqldb:3306/task_db")
settings = Settings()
