from django.shortcuts import render
from django.http import HttpResponse
from twitterapi import views
from .forms import twitterForm


# Create your views here.

urlArray = []
usersAdded = "None"


def indexer(request):
     if request.method == 'POST':
          form = twitterForm(request.POST)
          if form.is_valid():
               data = form.cleaned_data
               urlArray.extend(views.getImageUrlFile(data['twitterUserId']))
               return render(request, 'indexer/home.html', {'urlArray': urlArray, 'usersAdded': usersAdded})
     return render(request, 'indexer/home.html', {'urlArray': urlArray, 'usersAdded': usersAdded})

