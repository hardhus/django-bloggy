from django.urls import path
from mainpage import views


urlpatterns = [
    path("", views.index_main, name="index_main"),
]