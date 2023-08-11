from django.urls import path, re_path
from blog import views


urlpatterns = [
    path('', views.index, name='index'),
    path('add_post/', views.add_post, name='add_post'),
    path('<slug>/', views.post, name='post'),
]