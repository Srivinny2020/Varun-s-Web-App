from django.shortcuts import render
from newsapi import NewsApiClient


def Index(request):
    newsapi = NewsApiClient(api_key="78b9d599c4f94f8fa3afb1a5458928d6")
    topheadlines = newsapi.get_top_headlines(sources='espn')

    articles = topheadlines['articles']

    desc = []
    news = []
    img = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])

    mylist = zip(news, desc, img)

    return render(request, 'index.html', context={"mylist": mylist})


def worldnews(request):
    newsapi = NewsApiClient(api_key="78b9d599c4f94f8fa3afb1a5458928d6")
    topheadlines = newsapi.get_top_headlines(sources='worldnews')

    articles = topheadlines['articles']

    desc = []
    news = []
    img = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])

    mylist = zip(news, desc, img)

    return render(request, 'worldnews.html', context={"mylist": mylist})
