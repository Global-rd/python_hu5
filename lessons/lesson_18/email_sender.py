import smtplib #SIMPLE MAIL TRANSFER PROTOCOL
from email.mime.text import MIMEText # MULTI PURPOSE INTERNET MAIL EXTENSIONS
from email.mime.multipart import MIMEMultipart # multiple things to be present in the same email
from email.mime.base import MIMEBase # responsible for attachments
from email import encoders
from typing import Optional
from jinja2 import Template

class EmailSender:

    def __init__(self,
                 smtp_server: str,
                 smtp_port: int,
                 sender_email: str,
                 sender_password: str):

        self._smtp_server = smtp_server
        self._smtp_port = smtp_port
        self._sender_email = sender_email
        self._sender_password = sender_password

    def send_email(self,
                   recipients: list[str],
                   subject: str,
                   body: str,
                   attachments: Optional[list[str]]=None):

        msg = MIMEMultipart()
        msg["From"] = self._sender_email
        msg["To"] = ", ".join(recipients)
        msg["Subject"] = subject

        if "<html>" in body:
            msg.attach(MIMEText(body, 'html'))
        else:
            msg.attach(MIMEText(body, 'plain'))

        if attachments:
            for file_path in attachments:
                try:
                    with open(file_path, "rb") as attachment: #read binary
                        part = MIMEBase("application", "octet-stream") 
                        part.set_payload(attachment.read())
                        encoders.encode_base64(part)

                        part.add_header(
                            "Content-Disposition",
                            f"attachment; filename={file_path.split('/')[-1]}"
                        )
                        msg.attach(part)
                except Exception as e:
                    print(f"Failed to attach file {file_path}. Error: {e}")

        try:
            with smtplib.SMTP(self._smtp_server, self._smtp_port) as server:
                server.starttls()
                server.login(self._sender_email, self._sender_password)
                server.sendmail(self._sender_email, recipients, msg.as_string())
                print("Email sent successfully!")
        except Exception as e:
            print(f"Failed to send email: {e}")

    @staticmethod
    def render_email_template(template_path: str, context: dict):
        with open(template_path, "r") as file:
            template = file.read()

        jinja_template = Template(template)
        return jinja_template.render(context)

        
        



        