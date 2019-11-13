from django.contrib import admin

from .models import Post
from likes.models import Like
from unlikes.models import Unlike
from comments.models import Comment


class CommentInline(admin.TabularInline):
  model = Comment
  extra = 0


class LikeInline(admin.TabularInline):
  model = Like
  extra = 0


class UnlikeInline(admin.TabularInline):
  model = Unlike
  extra = 0


class PostAdmin(admin.ModelAdmin):
  list_display = ['title', 'description', 'created_at', 'owner']
  inlines = [LikeInline, UnlikeInline, CommentInline]

admin.site.register(Post, PostAdmin)
admin.site.register(Like)
admin.site.register(Unlike)
admin.site.register(Comment)
