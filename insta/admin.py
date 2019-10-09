from django.contrib import admin

from Insta.models import InstaUser, Like, Post, UserConnection

# Register your models here.
admin.site.register(Post)
admin.site.register(InstaUser)
admin.site.register(Like)
admin.site.register(UserConnection)