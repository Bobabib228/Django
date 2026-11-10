from django.contrib import admin
from django.urls import path, include
from django.views import View

from blog.views import PostListView

app_name = 'blog'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', PostListView.as_view(), name='post_list'),
]