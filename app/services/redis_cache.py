import redis.asyncio as redis
from app.config import get_settings

_redis_client = None 

def get_redis():
    global _redis_client
    if _redis_client is None:
        settings = get_settings()
        _redis_client = redis.Redis.from_url(
            settings.REDIS_URL,
            decode_responses=True
        )
    return _redis_client

async def set_cache(key: str, value: str, expire: int = 270):
    r = get_redis()
    await r.set(key, value, ex=expire)

async def get_cache(key: str):
    r = get_redis()
    return await r.get(key)
