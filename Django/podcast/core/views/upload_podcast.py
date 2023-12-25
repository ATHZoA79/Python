from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from core.forms import PodcastForm


@login_required
def upload_podcast(request):
    if request.method == "POST":
        form = PodcastForm(request.POST, request.FILES)
        if form.is_valid():
            podcast = form.save(commit=False)
            podcast.author = request.user
            podcast.save()
            return redirect("home")
          
    else:
        form = PodcastForm()
    form = PodcastForm()
    return render(request, "upload_podcast.html", context={"form": form})
