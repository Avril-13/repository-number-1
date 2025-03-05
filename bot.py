!pip install aiogram -q
!pip install aiogram aiohttp

import json
from aiogram import Bot, Dispatcher, types 
import logging  
import asyncio  
import sys  
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


API_TOKEN = " "


logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

url = 'https://raw.githubusercontent.com/vifirsanova/compling/main/tasks/task3/faq.json'
response = requests.get(url)
data = response.json()

data

keywords = {
    "цены": "цены, стоимость, заказ, оплата",
    "часы работы": "часы работы, время работы, доступность",
    "доставка": "доставка, сроки доставки, стоимость доставки, отслеживание",
    "возврат": "возврат, обмен, возврат товара, гарантия",
    "контакты": "связаться, телефон, email, адрес"
}


kb = [
    [
        KeyboardButton(text="О боте"),
        KeyboardButton(text="Помощь")  
    ]
]


keyboard = ReplyKeyboardMarkup(
    keyboard=kb, 
    resize_keyboard=True, 
    input_field_placeholder="Выберите действие" 
    )



@dp.message(Command("start"))
async def send_welcome(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_about = types.KeyboardButton("О компании")
    button_contact = types.KeyboardButton("Связаться с оператором")
    keyboard.add(button_about, button_contact)
    await message.answer("Добро пожаловать! Как я могу помочь?", reply_markup=keyboard)


@dp.message(lambda message: True)
async def handle_message(message: types.Message):
    user_query = message.text.lower()
    
    
    response_text = None
    for keyword in keywords.keys():
        if keyword in user_query:
            response_text = data.get(keywords[keyword], "Извините, я не нашел ответа на ваш вопрос.")
            break
    
    if response_text:
        await message.answer(response_text)
    else:
        await message.answer("Извините, я не понимаю ваш вопрос.")


@dp.message(lambda message: message.text == "О компании")
async def about_company(message: types.Message):
    await message.answer("Наша компания занимается доставкой товаров по всей стране.")


@dp.message (lambda message: message.text == "Связаться с оператором")
async def contact_operator(message: types.Message):
    await message.answer("Перевожу на оператора...")

if __name__ == '__main__':
    await main()
  
