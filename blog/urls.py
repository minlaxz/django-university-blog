from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_overview, name='blog_overview'),
    path('post/<int:pk>/', views.blog_detail, name='post_detail'),
    path("<category>/", views.blog_category, name="blog_category"),
]
