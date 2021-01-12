from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from .models import Blog as Post

# from pylaxz.utils import logxs

# Create your views here.
def blog_overview(request):

    post_res = {
        "posts": Post.objects.filter(published_date__lte=timezone.now()).order_by(
            "-published_date"
        )
    }
    return render(request, "blog/post_list.html", post_res)


def blog_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def blog_category(request, category):
    posts = Post.objects.filter(
        categories__name__contains=category
    ).order_by(
        '-created_on'
    )
    context = {
        "category": category,
        "posts": posts
    }
    return render(request, "blog/post_category.html", context)