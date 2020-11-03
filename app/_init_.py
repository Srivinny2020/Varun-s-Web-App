from flask import Flask, render.template
from newsapi import NewsApiClient

app = Flask(_name_)

@app.route('/')
def Index():
    newsapi = NewsApi(api_key="78b9d599c4f94f8fa3afb1a5458928d6")
    topheadlines = newsapi.get_top_headlines(sources="abc-news")

    articles = topheadlines['articles']

    descrip = []
    news = []
    image = []
	
    for i in range(len(articles)):
	varunarticles = articles[i]
	news.append(varunarticles['title'])
        descrip.append(varunarticles['description'])
	image.append(varunarticles['urlToImage'])

    varunlist = zip(news, descrip, image)
    return render.template('index.html', context = varunlist)

if _name_ == "_main_":
    app.run(debug=True)
