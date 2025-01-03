# Create your views here.
from django.shortcuts import render
from .models import FlowerFeed


def feed_view(request):
    flowerfeeds = FlowerFeed.objects.all()  # Query the model
    return render(request, 'feed.html', {'flowerfeed': flowerfeeds})  # Pass it to the template
