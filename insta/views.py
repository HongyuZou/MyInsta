from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from insta.models import Post
# Create your views here.

class HelloWorld(TemplateView):
    template_name = 'test.html'

class PostView(ListView):
    model = Post
    template_name = 'index.html'
    
