from twilio.rest import Client
import smtplib

TWILIO_SID = "AC9236af76dba3753b70eb65a6320c359e"
TWILIO_AUTH_TOKEN = "feb01e8490e9d5ff777b3f3f43a4e21b"
TWILIO_VIRTUAL_NUMBER = "+18053016232"
TWILIO_VERIFIED_NUMBER = "+972526453661"
MY_EMAIL = "omrirahmaniking@gmail.com"
MY_PASSWORD = "pmucjalqpxmnecqd"
EMAIL_PROVIDER_SMTP_ADDRESS = "smtp.gmail.com"


class NotificationManager:
    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )

        print(message.sid)

    def send_emails(self, emails, message, google_flight_link):
        with smtplib.SMTP(EMAIL_PROVIDER_SMTP_ADDRESS) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}\n{google_flight_link}".encode('utf-8')
                )