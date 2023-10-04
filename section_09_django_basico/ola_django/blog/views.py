from typing import Any

from blog.data import posts
from django.http import HttpRequest
from django.shortcuts import render


def blog(request):
    context = {
        # "text": "Estamos no Blog",
        "posts": posts,
    }
    return render(request, "blog/index.html", context)


def post(request: HttpRequest, id: int):
    found_post: dict[str, Any] | None = None

    for post in posts:
        if post["id"] == id:
            found_post = post
            break

    if found_post is None:
        raise Exception("Post não existe.")

    context = {
        "post": found_post,
        "title": found_post["title"],
    }
    return render(request, "blog/post_detail.html", context)


def exemplo(request):
    context = {"text": "Estamos no Exemplo", "title": "Exemplo"}
    return render(request, "blog/exemplo.html", context)
