# Requisito 6
from tech_news.database import search_news


def search_by_title(title):
    news = search_news({"title": {"$regex": title, "$options": "i"}})
    print(news)
    filtered_by_title = []
    for new in news:
        filtered_by_title.append((new['title'], new['url']))
    return filtered_by_title


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
