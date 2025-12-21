from app.utils.currencies import CURRENCIES_NAMES


async def start_handler(message):
    text = (
        "👋 Привіт! Я бот для відстеження курсів валют 💵\n\n"
        "📌 Як користуватись:\n"
        "/rate USD\n"
        "/rate EUR UAH\n"
        "💵 Доступні валюти:\n"
    )
    
    for code, name in CURRENCIES_NAMES.items():
        text += f"{code} - {name}\n"
    
    await message.answer(text)