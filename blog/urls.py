from django.contrib import admin
from django.urls import path, include
from django.views import View

from blog.views import PostListView, PostDetailView

app_name = 'blog'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
]