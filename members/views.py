from django.shortcuts import render

# Create your views here.

def members(req):
    return render(req, 'members/index.html', {})