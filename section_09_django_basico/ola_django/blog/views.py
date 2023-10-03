from django.http import HttpResponse

# from django.shortcuts import render


def blog(request):
    print("BLOG")
    return HttpResponse("BLOG do App")
