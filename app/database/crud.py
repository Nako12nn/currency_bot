from sqlalchemy import select
from .db import SessionLocal
from .models import Currency

async def create_currency(code: str, name: str):
    async with SessionLocal() as session:
        currency = Currency(code=code, name=name)
        session.add(currency)
        await session.commit()
        return currency
    
async def get_all_currencies():
    async with SessionLocal() as session:
        stmt = select(Currency)
        result = session.execute(stmt)
        currencies = result.all()
        return [row[0] for row in currencies]
    