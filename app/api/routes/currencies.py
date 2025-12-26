from fastapi import APIRouter 
from fastapi import HTTPException
from app.database.crud import get_all_currencies

router = APIRouter(prefix="/currencies", tags=["Currencies"])

@router.get("/")
async def list_currencies():
    try:
        return await get_all_currencies()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    