from django.contrib import admin 
from django.urls import include, path
from insta.views import HelloWorld, PostView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

# detailed view: int:pk means find model with such key and reder to the template provided
# by view 
urlpatterns = [
    path('', HelloWorld.as_view(), name="helloworld"),  
    path('posts/', PostView.as_view(), name="posts"),
    path('post/<int:pk>', PostDetailView.as_view(), name='post_detail'),
    path('post/new', PostCreateView.as_view(), name='make_post'),
    path('post/update/<int:pk>', PostUpdateView.as_view(), name='post_update'),
    path('post/delete/<int:pk>', PostDeleteView.as_view(), name='post_delete')
]