from email_sender import EmailSender
from telegram import Telegram
import os
from dotenv import load_dotenv


def main():
    load_dotenv()

    #email sending:

    email_sender = EmailSender(
        smtp_server="smtp.gmail.com",
        smtp_port=587,
        sender_email=os.environ.get("GMAIL_EMAIL"),
        sender_password=os.environ.get("GMAIL_PW")
    )

    html_body = EmailSender.render_email_template(template_path="lessons/lesson_18/email_template.html",
                                                  context={"user_name": "Marika",
                                                           "year": 2026})

    email_sender.send_email(recipients=["nigrushid@gmail.com"],
                            subject="Test",
                            body=html_body,
                            attachments=["lessons/lesson_18/test.csv"])

    telegram = Telegram(bot_token=os.environ.get("TELEGRAM_BOT_TOKEN"),
                        chat_id=os.environ.get("TELEGRAM_CHAT_ID"))

    telegram.send_telegram_message("This is a message from the class.")
    
if __name__ == "__main__":
    main()
