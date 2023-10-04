from blog.data import posts
from django.shortcuts import render


def blog(request):
    context = {
        "text": "Estamos no Blog",
        "posts": posts,
    }
    return render(request, "blog/index.html", context)


def exemplo(request):
    context = {"text": "Estamos no Exemplo", "title": "Exemplo"}
    return render(request, "blog/exemplo.html", context)
