from app.database.crud import get_all_currencies

async def currencies_handler(message):
    currencies = await get_all_currencies()

    if not currencies:
        await message.answer("Currency list is empty")
        return message
    
    text = "Available cyrrencies: "

    for currency in currency:
        text += f"{currency.code} - {currency.name}\n"

    text += "\nHow to use:\n/rate USD\n/rate EUR UAH"

    await message.answer(text)