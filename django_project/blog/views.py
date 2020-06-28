from django.shortcuts import render
from .models import Post


def home(request):
    
    return render(request, 'blogs/home.html')


def about(request):
    return render(request, 'blogs/about.html', {'title': 'About'})


def service(request):
    return render(request, 'blogs/service.html')

def poems(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blogs/poem.html', context)