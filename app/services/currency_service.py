import httpx 
import logging
import json
from app.services.redis_cache import get_cache, set_cache

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

API_URL = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json"

CACHE_EXPIRE = 270

async def get_rate(base: str, target = "UAH"):
    base = base.upper()
    target = target.upper()
    cache_key = f"rate:{base}:{target}"

    cached = await get_cache(cache_key)
    if cached:
        logger.info(f"Rate found in cache: {cache_key}")
        return json.loads(cached)

    try:
        async with httpx.AsyncClient(timeout=10.0) as client:
            resp = await client.get(API_URL)
        if resp.status_code != 200:
            logger.error(f"Bad status code {resp.status_code}")
            return {"error": f"API returned error {resp.status_code}"}       
   
        data = resp.json()

    except Exception:
        logger.exception("Network error while fetching rate")
        return{"error": "Network error"}

    rate_base = None
    date = None
    
    for currency in data:
        if currency["cc"] == base:
            rate_base = currency["rate"] 
            date = currency["exchangedate"]
            break

    if rate_base is None:
        return {"error": "Base currency not found"}
    
    if target == "UAH":
        result = {
            "base": base, 
            "target": "UAH", 
            "rate": rate_base, 
            "date": date
        }
    
    else: 
        rate_target = None
        
        for currency in data:
            if currency["cc"] == target:
                rate_target = currency["rate"] 
                break

        if rate_target is None:
            return {"error": "Target currency not found"}
    
        result = {
            "base": base, 
            "target": target, 
            "rate": round(rate_base / rate_target, 2), 
            "date": date
        }

    await set_cache(cache_key, json.dumps(result), expire=CACHE_EXPIRE)
    logger.info(f"Rate cached: {cache_key}")

    return result