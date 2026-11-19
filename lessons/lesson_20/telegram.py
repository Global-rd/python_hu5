import requests

class Telegram:

    def __init__(self, bot_token:str, chat_id:str):
        self._bot_token = bot_token
        self._chat_id = chat_id

    def send_telegram_message(self, message: str):

        url = f"https://api.telegram.org/bot{self._bot_token}/sendMessage"
        print(url)

        payload = {
            "chat_id": self._chat_id,
            "text": message
        }

        response = requests.post(url, json=payload)

        if response.status_code == 200:
            print("Telegram message sent successfully")
        else:
            print(f"Failed to send message. Status: {response.status_code}, error: {response.text}")
