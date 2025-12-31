from app.utils.currencies import CURRENCIES_NAMES


async def start_handler(message):
    text = (
        "👋 Hi! I am a bot for tracking currency exchange rates 💵\n\n"
        "📌 How to use:\n"
        "/rate USD\n"
        "/rate EUR UAH\n"
        "💵  Available currencies:\n"
    )
    
    for code, name in CURRENCIES_NAMES.items():
        text += f"{code} - {name}\n"
    
    await message.answer(text)