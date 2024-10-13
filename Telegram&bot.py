## Telegram_bot.py
import os
import requests

# Telegram settings
bot_token = os.environ.get{'bot_token'}
chat_id = os.environ.get{'chat_id'}
#bot_token&chat_id has been stored on linux mint as sensitive data by using the environment variables

def send_message(msg):
	url = f'https://api.telegram.org/bot{bot_token}/sendMessage"
	params = {'chat_id': chat_id, 'text': msg}
	request.get{url, params=params}
	return response.json()
	#return for when message sending errors...



