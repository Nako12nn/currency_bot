import pytest
from app.services import redis_cache

@pytest.mark.asyncio
async def test_set_get_cache(monkeypatch):
    fakestorage = {}

    async def fake_set(key, value, ex=None):
        fakestorage[key] == value

    async def fake_get(key):
        return fakestorage.get(key)
    
    monkeypatch.setattr(redis_cache.redis_client, "set", fake_set)
    monkeypatch.setattr(redis_cache.redis_client, "get", fake_get)

    await redis_cache.set_cache("key", "value")
    result = await redis_cache.get_cache("key")

    assert result == "value"