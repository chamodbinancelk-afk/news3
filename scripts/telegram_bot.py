import os
import time
import requests
import telepot
from telepot.loop import MessageLoop
from dotenv import load_dotenv

load_dotenv()

# Importing API and Tokens from dotenv file.
TOKEN = os.getenv('8299929776:AAGKU7rkfakmDBXdgiGSWzAHPgLRJs-twZg')
NEWS_API_KEY = os.getenv('https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=3833ef78b7a64b69ab901ca66e49d6dc')
TARGET_CHAT_ID = os.getenv('-1003177936060')


def fetch_technology_news(api_key, country='in', category='technology', num_articles=5):
    base_url = 'https://newsapi.org/v2/top-headlines'
    params = {
        'country': country,
        'category': category,
        'apiKey': api_key,
        'pageSize': num_articles
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()

        if data['status'] == 'ok':
            articles = data['articles']
            return articles
        else:
            print(f"Error: {data['message']}")
            return []

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return []

def send_news_on_start(api_key, chat_id):
    articles = fetch_technology_news(api_key)

    if articles:
        for idx, article in enumerate(articles, start=1):
            title = article['title']
            url = article['url']
            news_message = f"{idx}. {title}\n   {url}\n"
            bot.sendMessage(chat_id, news_message)
    else:
        bot.sendMessage(chat_id, "Error fetching news. Please try again later.")



# Create the bot with the provided token
bot = telepot.Bot(TOKEN)

# Send news when the bot starts
send_news_on_start(NEWS_API_KEY, TARGET_CHAT_ID)


