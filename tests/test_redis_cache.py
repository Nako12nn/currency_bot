import pytest
from types import SimpleNamespace
from app.services import redis_cache

@pytest.mark.asyncio
async def test_set_get_cache(monkeypatch):
    fakestorage = {}

    async def fake_set(key, value, ex=None):
        fakestorage[key] = value

    async def fake_get(key):
        return fakestorage.get(key)

    fake_settings = SimpleNamespace(
        REDIS_URL="redis://fake:6379"
    )

    monkeypatch.setattr(
        "app.services.redis_cache.get_settings",
        lambda: fake_settings
    )

    client = redis_cache.get_redis()
    monkeypatch.setattr(client, "set", fake_set)
    monkeypatch.setattr(client, "get", fake_get)

    await redis_cache.set_cache("key", "value")
    result = await redis_cache.get_cache("key")

    assert result == "value"