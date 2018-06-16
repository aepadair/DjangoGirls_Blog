from django.shortcuts import render
from django.utils import timezone
from .models import Post
# Created a function (def) called post list, that takes request and returns a function 
# that will render our template our template blog/post_list.html

#we want published blog posts sorted by published date 
# we get this piece of code inside by adding it to the function 'def post_list(request)'

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})