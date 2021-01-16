from django.shortcuts import render

# Create your views here.
def activity_page(req):
    return render(
        req, "ecactivity/index.html", {"txt": "Application named 'EC Activity'"}
    )
