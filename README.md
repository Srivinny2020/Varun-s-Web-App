# Varun-s-Web-App

from flask import Flask
from news api import NewsApiClient

app = Flask(_VNews_)

@app.route('https://VNews.com')
def Index():
      newsapi = NewsApiClient(api_key = "78b9d599c4f94f8fa3afb1a5458928d6")
      topheadlines = newsapi.get_top_headlines(sources = "abc-news")
