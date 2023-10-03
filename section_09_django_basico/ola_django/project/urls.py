from django.contrib import admin
from django.http import HttpResponse
from django.urls import path


def home(request):
    print("HOME")
    return HttpResponse("HOME")


def my_view(request):
    print("BLOG")
    return HttpResponse("BLOG")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home),
    path("blog/", my_view),
]
