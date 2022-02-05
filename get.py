import requests
from bs4 import BeautifulSoup
from db_connect import tvn, tvp
import datetime

def get_tvn():
    page_url = 'http://tvn24.pl/'
    page = requests.get(page_url)
    soup = BeautifulSoup(page.content, 'html.parser')
    headlines = soup.find_all(class_='article-header')
    top_story = soup.find(class_='top-story__header')
    item = ' '.join(top_story.text.split())
    entry = {
        "headline": item,
        "type": "top-story",
        "date": datetime.datetime.utcnow()
    }
    tvn.insert_one(entry)

    for i in range(9):
        item = ' '.join(headlines[i].text.split())
        entry = {
            "headline": item,
            "type": "regular-news",
            "date": datetime.datetime.utcnow()
        }
        tvn.insert_one(entry)
    return

def get_tvp():
    page_url = 'http://tvp.info/'
    page = requests.get(page_url)
    soup = BeautifulSoup(page.content, 'html.parser')
    top_story = soup.find(class_='main-module__news-title')
    headlines = soup.find_all(class_=lambda x: x and ((x.endswith('__title') or x.endswith('--title')) and not x.endswith('report__title')))
    item = ' '.join(top_story.text.split())
    entry = {
        "headline": item,
        "type": "top-story",
        "date": datetime.datetime.utcnow()
    }
    tvp.insert_one(entry)
    for i in range(2, 11):
        item = ' '.join(headlines[i].text.split())
        entry = {
            "headline": item,
            "type": "regular-news",
            "date": datetime.datetime.utcnow()
        }
        tvp.insert_one(entry)

def main():
    get_tvp()
    get_tvn()

if __name__ == "__main__":
    main()
