from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

posts = [
    {
        'author': 'Andy',
        'title': 'First Post',
        'content': 'first post',
        'posted_at': '2023-1-1',
    },
    {
        'author': 'Betty',
        'title': 'Second Post',
        'content': 'second post',
        'posted_at': '2023-1-2',
    },
]

# Create your views here.
# 這個函式被urls呼叫作為路由進入點
def home(request):
    context = {
        'posts': Post.objects.all(),
    }
    return render(request, 'blog/index.html', context)

def about(request):
    return render(request, 'blog/about.html')