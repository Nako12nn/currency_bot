from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from app.config import settings
from sqlalchemy.orm import DeclarativeBase
from contextlib import asynccontextmanager

engine = create_async_engine(
    settings.DATABASE_URL,
    echo=True,
)

SessionLocal = async_sessionmaker(
    engine,
    expire_on_commit=False
)

class Base(DeclarativeBase):
    pass

@asynccontextmanager
async def get_db():
    async with SessionLocal() as session:
        yield session

async def close_db():
    await engine.dispose()