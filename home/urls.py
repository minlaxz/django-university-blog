from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page_uid'),
    path('hidden/', views.hidden_home, name='hidden_home_uid'),

]
