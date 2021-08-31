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
    def get_news(date: str) -> list:
        parameters = {
            'q': 'Tesla',
            'from': date,
            'sortBy': 'popularity',
            'apiKey': '3a863125fd28453880e620cfee810b09'
        }
        news_data = requests.get(url='https://newsapi.org/v2/everything', params=parameters).json()
        return news_data['articles']