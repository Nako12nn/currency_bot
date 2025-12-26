from fastapi import FastAPI
from app.api.routes.currencies import router as currencies_router

app = FastAPI(title="Currency API")
app.include_router(currencies_router)

@app.get("/health")
async def health():
    return {"status": "ok "}
#CMD ["python", "app/main.py"]