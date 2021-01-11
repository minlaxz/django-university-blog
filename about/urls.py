from django.urls import path
from . import views

urlpatterns = [
    path('', views.about_page, name='about_page_uid'),
    path('hidden/', views.hidden_about, name='about_page_hidden_uid'),
]
