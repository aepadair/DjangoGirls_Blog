from django.shortcuts import render

# Created a function (def) called post list, that takes request and returns a function 
# that will render our template our template blog/post_list.html
def post_list(request):
    return render(request, 'blog/post_list.html', {})
