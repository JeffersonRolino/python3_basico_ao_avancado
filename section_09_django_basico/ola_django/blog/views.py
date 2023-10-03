from django.http import HttpResponse

# from django.shortcuts import render


def blog(request):
    print("BLOG")
    return HttpResponse("BLOG do App 1")


def exemplo(request):
    print("Exemplo")
    return HttpResponse("Exemplo do App 1")
