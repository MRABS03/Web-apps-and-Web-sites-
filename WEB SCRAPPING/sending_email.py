import smtplib
import ssl

host = "smtp.gmail.com"
PASSWORD = 'fazh oumh wrni zfju'
SENDER = "abdullahbinsalman2003@gmail.com"
RECEIVER = "abdullahbinsalman2003@gmail.com"
port = 465


def send_email(content):
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(SENDER, PASSWORD)
        server.sendmail(SENDER, RECEIVER, content)
        print("Email Sent!")
