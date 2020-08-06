from django.contrib import admin
from .models import Myinfo, Board, Post, Comment, GuestBook

admin.site.register(Myinfo)
admin.site.register(Board)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(GuestBook)

