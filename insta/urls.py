from django.contrib import admin 
from django.urls import include, path
from insta.views import HelloWorld, PostView

urlpatterns = [
    path('', HelloWorld.as_view(), name="helloworld"),  
    path('posts/', PostView.as_view(), name="posts")
]