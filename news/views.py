
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
