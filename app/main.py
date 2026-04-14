from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/")
def home():
    return {
        "version": os.getenv("APP_VERSION", "v1.0"),
        "message": {"msg": "hello CI/CD"},
    }
