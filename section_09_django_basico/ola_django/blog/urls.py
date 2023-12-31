from django.urls import path

from . import views

app_name = "blog"

# blog/
urlpatterns = [
    path("", views.blog, name="home"),
    path("<int:id>/", views.post, name="post"),
    path("exemplo/", views.exemplo, name="exemplo"),
]
