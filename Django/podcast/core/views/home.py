from django.shortcuts import render
from core.models import Podcast


def home(request):
    return render(request, "index.html")
