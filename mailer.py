from env import MAIN_EMAIL, MAIN_EMAIL_PASSWORD, TEST_EMAIL, GMAIL_SMTP
import smtplib


def send_mail(message):
    with smtplib.SMTP(GMAIL_SMTP) as connection:
        connection.starttls()
        connection.login(user=MAIN_EMAIL, password=MAIN_EMAIL_PASSWORD)
        connection.sendmail(
            from_addr=MAIN_EMAIL,
            to_addrs=TEST_EMAIL,
            msg=message.encode('utf-8')
        )
        print(f'Sent to {TEST_EMAIL}')
