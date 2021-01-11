from django.shortcuts import render

# Create your views here.
def about_page(req):
    return render(req, 'about/index.html', {"txt":"Application named 'About'"})

def hidden_about(req):
    return render(req, 'about/hidden.html', {})