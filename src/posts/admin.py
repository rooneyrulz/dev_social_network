from django.contrib import admin

from .models import Post
from likes.models import Like
from unlikes.models import Unlike
from comments.models import Comment

admin.site.register(Post)
admin.site.register(Like)
admin.site.register(Unlike)
admin.site.register(Comment)
