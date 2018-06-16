from django.conf.urls import url
from . import views


#asssinging view
#so name= is the name of the url that will be used to identify the view
urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
]