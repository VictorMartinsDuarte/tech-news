import requests
import time
from parsel import Selector

from tech_news.database import create_news


# Requisito 1
def fetch(url, timeout=3):
    user_agent = {"user-agent": "Fake user-agent"}
    try:
        response = requests.get(url, timeout=timeout, headers=user_agent)
        response.raise_for_status()
        time.sleep(1)
    except (requests.HTTPError, requests.ReadTimeout):
        return None
    else:
        return response.text


# Requisito 2
def scrape_novidades(html_content):
    try:
        selector = Selector(html_content)
        news_links = selector.css("a.cs-overlay-link ::attr(href)").getall()
    except html_content == "":
        return []
    else:
        return news_links


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    selector_css_string = "a.next ::attr(href)"
    return selector.css(selector_css_string).get()


# Requisito 4
def scrape_noticia(html_content):
    selector = Selector(html_content)
    url = selector.css("head link[rel=canonical] ::attr(href)").get()
    title = selector.css("h1.entry-title::text").get()
    timestamp = selector.css("li.meta-date::text").get()
    writer = selector.css("span.fn a::text").get()
    comments = selector.css("h5.title-block").get()
    comments_count = 0
    for s in comments.split():
        if s.isdigit():
            comments_count = int(s)
    summary = selector.css(
        "div.entry-content > p:nth-of-type(1) *::text"
    ).getall()
    tags = selector.css("li a[rel=tag]::text").getall()
    category = selector.css("span.label::text").get()
    scraped_dict = {
        "url": url,
        "title": title.strip(),
        "timestamp": timestamp,
        "writer": writer.strip(),
        "comments_count": comments_count,
        "summary": ''.join(summary).strip(),
        "tags": tags,
        "category": category,
    }
    return scraped_dict


# Requisito 5
def get_tech_news(amount):
    url = "https://blog.betrybe.com/"
    news = []
    while len(news) < amount:
        news_links = scrape_novidades(fetch(url))
        for link in news_links:
            if len(news) < amount:
                news.append(scrape_noticia(fetch(link)))
        url = scrape_next_page_link(fetch(url))
    create_news(news)
    return news
