from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'is_published')
    list_filter = ('title', 'is_published')
    search_fields = ('title', 'is_published')
