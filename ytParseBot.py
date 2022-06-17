import hashlib

# import requests
# from bs4 import BeautifulSoup
# import re
from youtube_search import YoutubeSearch
from config import TOKEN
from aiogram import Bot, types, utils
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import InputTextMessageContent, InlineQueryResultArticle
import os

#через requests + BeaBeautifulSoup (нужно чистить найденные значения [не лучший вариант])
# def searcher():
#     response = requests.get('https://www.youtube.com/results?search_query=python')
#     soup = BeautifulSoup(response.content, 'html.parser')
#     search = soup.find_all('script')[32]
#     key = '"videoId":"'
#     data = re.findall(str(search), key=r"([^*]{11}")
#     print(data)

def searcher(text):
    res = YoutubeSearch(text, max_results=10).to_dict()
    # with open('text.py', 'w', encoding='utf-8') as r:
    #     r.write(str(res))
    return res

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.inline_handler()
async def inline_handler(query : types.InlineQuery):
    text = query.query or 'echo'
    links = searcher(text)

    articles = [types.InlineQueryResultArticle(
        id = hashlib.md5(f'{link["id"]}'.encode()).hexdigest(),
        title = f'{link["title"]}',
        url = f'https://www.youtube.con/watch?v={link["id"]}',
        input_message_content=types.InputTextMessageContent(
            message_text=f'https://www.youtube.com/watch?v={link["id"]}')
    )for link in links]

    await query.answer(articles, cache_time=60, is_personal=True)

executor.start_polling(dp, skip_updates=True)