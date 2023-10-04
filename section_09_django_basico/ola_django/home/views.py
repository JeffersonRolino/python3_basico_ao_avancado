from django.shortcuts import render


def home(request):
    context = {"text": "Olá home"}
    print("HOME")
    return render(request, "home/index.html", context)
