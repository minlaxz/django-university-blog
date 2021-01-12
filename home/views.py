from django.shortcuts import render

# Create your views here.

def home_page(req):
    return render(req, 'home/index.html', {})


def hidden_home(req):
    return render(req, 'home/hidden_home.html', {})
