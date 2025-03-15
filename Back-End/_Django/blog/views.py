from django.shortcuts import render
from typing import Any
from django.http import HttpRequest, Http404

from blog.data import posts


def blog(request):

    context = {
        'text': 'Estamos na blog',
        'posts': posts,
    }

    return render(
        request,
        "blog/index.html",
        context
    )


def post(request: HttpRequest, post_id: int):
    found_post: dict[str, Any] | None = None

    for post in posts:
        if post['id'] == post_id:
            found_post = post
            break

    if found_post is None:
        raise Http404('Post not found')

    context = {
        'title': found_post['title'] + ' - ',
        'post': found_post,
    }

    return render(
        request,
        "blog/post.html",
        context
    )


def exemplo(request):
    return render(request, "blog/exemplo.html", {'text': ' Estamos no exemplo'})
