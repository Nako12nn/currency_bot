import asyncio
from app.database.crud import create_currency

async def seed():
    await create_currency("USD", "US Dollar")
    await create_currency("EUR", "Euro")
    await create_currency("UAH", "Ukrainian Hryvnia")

if __name__ == "__main__":
    asyncio.run(seed())