from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Category

# Create your views here.
# M - models.py
# V - html
# C - views.py

# M - models.py
# T - template
# V - views.py

def home(request):
    return HttpResponse('Olá mundo!')

def home_param(request, id):
    return HttpResponse('Olá mundo! %s' % id)

def post_list(request):
    if 'category_id' in request.GET:
        category = Category.objects.get(id=request.GET['category_id'])
        posts = Post.objects.filter(categories=category)
    else:
        posts = Post.objects.all()

    categories = Category.objects.all()
    return render(request, 'post_list.html', {
        'posts': posts,
        'categories': categories
    })

def post_show(request, post_id):
    post = Post.objects.get(id=post_id)
    categories = Category.objects.all()
    return render(request, 'post_show.html', {
        'post': post, 
        'categories': categories
    })