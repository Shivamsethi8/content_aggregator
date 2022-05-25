
from django.shortcuts import render
from newsapi import NewsApiClient


def Index(request):
    newsapi = NewsApiClient(api_key="fd04ae45b67e45e08fe62e82e0c357f3")
    topheadlines = newsapi.get_top_headlines(sources='the-times-of-india')

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

    return render(request, 'newapi.html', context={"mylist": mylist})


def bbc(request):
    newsapi = NewsApiClient(api_key="fd04ae45b67e45e08fe62e82e0c357f3")
    topheadlines = newsapi.get_top_headlines(sources='bbc-news')

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

    return render(request, 'newapi.html', context={"mylist": mylist})

from django.shortcuts import render
import requests
api_key="8955b7d282574587a9719edeb4f1fe73"


def home(request):
    country = request.GET.get('country')
    category = request.GET.get('category')

    if country:
        url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={"8955b7d282574587a9719edeb4f1fe73"}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
    else:
        url = f'https://newsapi.org/v2/top-headlines?category={category}&apiKey={"8955b7d282574587a9719edeb4f1fe73"}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']



    context = {
        'articles' : articles
    }

    return render(request, 'tempN/news_api.html', context)

