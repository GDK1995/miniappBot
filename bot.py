import asyncio
import logging
import aiohttp
import json

from aiogram import Bot, Dispatcher, types, F
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters import CommandStart

logging.basicConfig(level=logging.INFO)

bot = Bot(token='7572571958:AAFiRvI35qUvL6wz-wRjdXqfvaogy6La-Zs')
dp = Dispatcher()

API_REGISTRATION_URL = "https://goodmood.kz/api/v1/user/accounts/create/"

@dp.message(CommandStart())
async def start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(
                    text="Open WebApp",
                    web_app=types.WebAppInfo(url="https://miniapp.excourse.kz/?v=6")
                )
            ]
        ],
        resize_keyboard=True
    )

    await message.answer(
        "Привет! Нажми на кнопку ниже, чтобы открыть WebApp:",
        reply_markup=keyboard
    )

@dp.message(F.web_app_data)
async def parse_data(message: types.Message):
    print(">>BOT RECEIVED WEB APP DATA", message.from_user.id)
    print(">BOT RECEIVED WEB APP DATA", message.web_app_data.data)
    try:
        data = json.loads(message.web_app_data.data)
        logging.info("WebApp data received: %s", data)

        first_name = data.get("first_name")
        birth_date = data.get("birth_date")
        email = data.get("email")
        last_name = data.get("last_name")
        password = data.get("password")
        phone = data.get("phone")
        host = data.get("host")
        utmContent = data.get("utmContent")
        utmSource = data.get("utmSource")
        utmMedium = data.get("utmMedium")
        utmTerm = data.get("utmTerm")
        utmCampaign = data.get("utmCampaign")

        if first_name:
            await bot.send_message(
                message.from_user.id,
                f"Данные от веб-приложения: {first_name}"
            )
        async with aiohttp.ClientSession() as session:
            payload = {
                "first_name": first_name,
                "birth_date": birth_date,
                "email": email,
                "last_name": last_name,
                "password": password,
                "phone": phone,
                "host": host,
                "utmContent": utmContent,
                "utmSource": utmSource,
                "utmMedium": utmMedium,
                "utmTerm": utmTerm,
                "utmCampaign": utmCampaign
                # "telegram_id": message.from_user.id
            }
            print('payload', payload)

            try:
                async with session.post(API_REGISTRATION_URL, json=payload) as resp:
                    if resp.status in (200, 201):
                        result = await resp.json()
                        await message.answer(f"✅ Успешная регистрация!\nЛогин: {result['email']}")
                    else:
                        await message.answer(f"⚠️ Ошибка при регистрации. Код: {resp.status}")
            except Exception as e:
                logging.error("API request failed: %s", e)
                await message.answer("🚫 Ошибка при соединении с сервером регистрации.")

    except json.JSONDecodeError:
        await bot.send_message(
            message.from_user.id,
            "Ошибка: данные от WebApp не в формате JSON"
        )

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())