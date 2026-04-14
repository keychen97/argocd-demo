from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/")
def home():
    return {
        "version": os.getenv("APP_VERSION", "v3.0"),
        "status": "ok",
    }
