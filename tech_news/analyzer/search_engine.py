# Requisito 6
from tech_news.database import search_news
from datetime import datetime as dt


def search_by_title(title):
    news = search_news({"title": {"$regex": title, "$options": "i"}})
    print(news)
    filtered_by_title = []
    for new in news:
        filtered_by_title.append((new["title"], new["url"]))
    return filtered_by_title


# Requisito 7
def search_by_date(date):
    try:
        news = search_news({
            "timestamp": dt.strptime(date, "%Y-%m-%d").strftime("%d/%m/%Y")})
        return [(new["title"], new["url"]) for new in news]
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_tag(tag):
    news = search_news({"tags": {"$regex": tag, "$options": "i"}})
    return [(new["title"], new["url"]) for new in news]


# Requisito 9
def search_by_category(category):
    news = search_news({"category": {"$regex": category, "$options": "i"}})
    return [(new["title"], new["url"]) for new in news]
