from operator import ne
import requests
import time
from parsel import Selector


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
        news_links = selector.css('a.cs-overlay-link ::attr(href)').getall()
    except html_content == "":
        return []
    else:
        return news_links


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    selector_css_string = 'a.next ::attr(href)'
    return selector.css(selector_css_string).get()


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
