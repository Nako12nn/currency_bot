import redis.asyncio as redis
from app.config import settings

redis_client = redis.Redis.from_url(settings.redis_url, decode_responses=True)

async def set_cache(key: str, value: str, expire: int = 270):
    await redis_client.set(key, value, ex=expire)

async def get_cache(key: str):
    return await redis_client.get(key)