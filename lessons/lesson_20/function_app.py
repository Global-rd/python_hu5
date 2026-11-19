import azure.functions as func
import logging
from telegram import Telegram
import os

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

@app.route(route="f_pythonhu5")
def f_pythonhu5(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('We received a request, yay!.')

    telegram = Telegram(bot_token=os.environ.get("TELEGRAM_BOT_TOKEN"),
                        chat_id=os.environ.get("TELEGRAM_CHAT_ID"))

    telegram.send_telegram_message("This is a message from the class.")

    challenge = req.params.get("challenge")

    if challenge:
        return func.HttpResponse(challenge, status_code=200)
    return func.HttpResponse("all good!", status_code=200)



