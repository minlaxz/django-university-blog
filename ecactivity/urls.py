from django.urls import path
from . import views

urlpatterns = [
    path('', views.activity_page, name='activity_page_uid'),
]
