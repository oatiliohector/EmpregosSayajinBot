import os
import requests
from dotenv import load_dotenv

load_dotenv()


class TelegramBot:
    def __init__(self, bot_id=None):
        self.bot_id = bot_id or os.getenv("BOT_SECRET_ID")
        if not self.bot_id:
            raise ValueError("BOT_SECRET_ID is missing in environment variables")

    def send_message(self, chat_id, message):
        url = f"https://api.telegram.org/bot{self.bot_id}/sendMessage"

        try:
            response = requests.post(url, json={"chat_id": chat_id, "text": message})
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as error:
            print(f"Error sending message: {error}")
            return {"error": str(error)}
