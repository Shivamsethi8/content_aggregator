
from app.models import *
from django.shortcuts import render,redirect
from django.http  import HttpResponse
import feedparser

from programming.models import PyContent, ProgContent


def updateprog(request):
    # -------python----------------
    url = feedparser.parse(
        "https://medium.com/feed/tag/programming"
    )
    for i in range(10):
        info = url.entries[i]
        content = ProgContent()
        content.headline = info.title
        # -----finding image link
        desc = info.description
        start = desc.find("img src=")
        end = desc.find("width")

        print(desc[end:])
        desc = desc[start + 9:end - 2:]
        print("-----------------------------")
        print(desc)

        # ---------------
        content.img = desc
        content.url = info.link
        content.save()

    return redirect('/')

def home(request):

    progcontent = ProgContent.objects.all()

    context = {
        'progcontent': progcontent,


    }
    return render(request,'D:/workspace/content_aggregator/programming/tempP.html',context)