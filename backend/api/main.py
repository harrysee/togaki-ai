# backend/api/main.py

from fastapi import FastAPI
from api.routers import router as api_router  # ← 이 부분이 router를 찾을 수 있어야 함

app = FastAPI()
app.include_router(api_router)

@app.get("/")
def root():
    return {"message": "Hello from togaki-ai"}
