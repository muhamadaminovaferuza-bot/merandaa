from django.shortcuts import render

def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def categories(request):
    return render(request, 'categories.html')

def index(request):
    return render(request, 'index.html')

def blog_single(request):
    return render(request, 'blog-single.html')