from django.shortcuts import render
from django.http import HttpResponse
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import TwitterApi

# Create your views here.

urlArray = TwitterApi.getImageUrlFile("hideo_kojima_en")

print (urlArray)

def indexer(request):
    return HttpResponse("A")

