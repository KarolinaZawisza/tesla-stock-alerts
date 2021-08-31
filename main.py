import smtplib
from tesla_stocks import get_stock_data
from news import News
import datetime as dt
from env import MAIN_EMAIL, MAIN_EMAIL_PASSWORD, TEST_EMAIL, GMAIL_SMTP

news_information: str
today_articles = []
stock_information = ''

# YYYY-MM-DD for getting news
nowYMD = dt.datetime.now().strftime('%Y-%m-%d')
# DD.MM.YYYY for subject of the message
nowDMY = dt.datetime.now().strftime('%d.%m.%Y')

new_articles = []
for new_art in News.get_news(nowYMD):
    article = News(
        new_art['author'],
        new_art['title'],
        new_art['description'],
        new_art['content'],
        new_art['url'],
        new_art['publishedAt'],
    )
    new_articles.append(article)

for art in range(0, 5):
    formatted_title = new_articles[art].title.replace('\u2026', "'")
    formatted_author = new_articles[art].author.replace('\u2026', "'")
    formatted_desc = new_articles[art].description.replace('\u2026', "'")

    news_information = f'Title: {formatted_title}\n' \
                       f'Author: {formatted_author}\n\n' \
                       f'{formatted_desc}\n\n' \
                       f'Find out more: {new_articles[art].url}'
    today_articles.append(news_information)

last_prices = get_stock_data()
stock_value_difference = float(last_prices[0]) - float(last_prices[1])
percentage_diff = stock_value_difference / float(last_prices[0]) * 100

if stock_value_difference > 0:
    stock_information = f'Tesla\'s stock value raised for {round(stock_value_difference, 3)}' \
                        f' ({round(percentage_diff, 2)}%) till yesterday closing!'
elif stock_value_difference < 0:
    stock_information = f'Tesla\'s stock value drop for {round(stock_value_difference, 3)}' \
                        f' ({round(percentage_diff, 2)}%) till yesterday closing!'

message = f'SUBJECT: Daily stock information: TESLA ({nowDMY})\n' \
          f'Welcome to daily stock information for TESLA!\n' \
          f'Current Tesla\'s stock value: {last_prices[2]}\n' \
          f'{stock_information}\n\n\n' \
          f'Important to know: \n\n' \
          f'{today_articles[0]}\n\n\n' \
          f'{today_articles[1]}\n\n\n' \
          f'{today_articles[2]}'

with smtplib.SMTP(GMAIL_SMTP) as connection:
    connection.starttls()
    connection.login(user=MAIN_EMAIL, password=MAIN_EMAIL_PASSWORD)
    connection.sendmail(
        from_addr=MAIN_EMAIL,
        to_addrs=TEST_EMAIL,
        msg=message
    )
    print('Sent.')