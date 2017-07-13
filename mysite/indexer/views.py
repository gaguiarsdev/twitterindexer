from django.shortcuts import render
from django.http import HttpResponse
from twitterapi import views


# Create your views here.

urlArray = views.getImageUrlFile("hideo_kojima_en")

print (urlArray)

def indexer(request):
     return render(request, 'indexer/home.html', {'urlArray': urlArray })
