import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from django.template.loader import render_to_string
# import environ
from email.message import EmailMessage
import smtplib
import asyncio                   


class environ():
    class Env():
        class read_env():
            pass 


env = environ.Env() 
environ.Env.read_env()

# sender_email = env('EMAIL_SENDER')
# password = env('EMAIL_PASSWORD')

sender_email = 'kkkk'
password = 'kkkkk'


class MailServices():
    def forget_password_mail(*args ,**kwargs):
        receiver_email = kwargs['email']
        token = kwargs['token']
        uuidb64 = kwargs['uuidb64']
        message = MIMEMultipart("alternative")
        message["Subject"] = "Reset your Buskeit password"
        message["From"] = sender_email
        message["To"] = receiver_email
        reset_link = f'http://127.0.0.1:3000/password/{token}/{uuidb64}/reset'
        print('***'*100)
        print(reset_link)
        print('***'*100)
        html = render_to_string('accounts/password-reset-mail.html', {'reset_link': reset_link})
        part = MIMEText(html, "html")
        # Add HTML/plain-text parts to MIMEMultipart message
        message.attach(part)
        # Create secure connection with server and send email
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(
                sender_email, receiver_email, message.as_string()
            )








