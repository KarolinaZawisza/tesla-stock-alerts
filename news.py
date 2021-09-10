import requests


class News:

    def __init__(self, author, title, description, content, url, published_at):
        self.author = author
        self.title = title
        self.description = description
        self.content = content
        self.url = url
        self.published_at = published_at

    @staticmethod
    def create_news_from_raw_data(next_article):
        return News(
            next_article['author'],
            next_article['title'],
            next_article['description'],
            next_article['content'],
            next_article['url'],
            next_article['publishedAt'],
            )

    @staticmethod
    def get_news(date: str) -> list:
        parameters = {
            'q': 'Tesla',
            'from': date,
            'sortBy': 'popularity',
            'apiKey': '3a863125fd28453880e620cfee810b09'
        }
        news_data = requests.get(url='https://newsapi.org/v2/everything', params=parameters).json()
        return news_data['articles']

    @staticmethod
    def create_article(title: str, author: str, description: str, url: str) -> str:
        news_information = f'Title: {title}\n' \
                            f'Author: {author}\n\n' \
                            f'{description}\n\n' \
                            f'Find out more: {url}'

        return news_information
