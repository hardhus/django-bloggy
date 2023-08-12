from django.shortcuts import render, redirect
from blog.views import index as blog_index
from django.urls import reverse

# Create your views here.
def index_main(request):
    print("test")
    blog_index_url = reverse("index")
    return redirect(blog_index_url)