from fastapi import FastAPI
from core.config import settings

app = FastAPI(title=settings.PROJECT_TITLE)

@app.get("/")
def index():
    return {"msg" : "hello"}



