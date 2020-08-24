from django.urls import path

from .views import (
    PostDetailView,
)
from . import views
urlpatterns = [
    path('', views.blog, name='blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
]