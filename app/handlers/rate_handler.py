from app.services.currency_service import get_rate

async def rate_handler(message):
    text = message.text
    parts = text.split()

    if len(parts) == 1:
        await message.answer("Please select your currency /rate USD")
        return
    
    base = parts[1].upper()
    target = parts[2].upper() if len(parts) >= 3 else "UAH"

    result = await get_rate(base, target)

    if "error" in result:
        await message.answer(result["error"])
        return
    
    base_currency = result["base"]
    target_currency = result["target"]
    rate = round(result["rate"], 2)
    date = result["date"]

    text_to_send = f"1 {base_currency} = {rate} {target_currency} (на {date}) 🪙"
    await message.answer(text_to_send)

