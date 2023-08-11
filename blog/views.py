from django.shortcuts import render, get_object_or_404, redirect

from blog.models import Post
from blog.forms import PostForm

# helper function
def encode_url(url):
    return url.replace(" ", "_")

def get_popular_posts(count):
    return Post.objects.order_by("-views")[:count]

# Create your views here.
def index(request):
    latest_posts = Post.objects.all().order_by("-created_at")
    popular_posts = get_popular_posts(5)
    context = {
        "latest_posts": latest_posts,
        'popular_posts': popular_posts,
    }
    for post in latest_posts:
        post.url = encode_url(post.title)
    for popular_post in popular_posts:
        popular_post.url = encode_url(post.title)
    return render(request, "blog/index.html", context)

def post(request, slug):
    single_post = get_object_or_404(Post, slug=slug)
    popular_posts = get_popular_posts(5)
    single_post.views += 1
    single_post.save()
    context = {
        "single_post": single_post,
        "popular_posts": popular_posts,
    }
    return render(request, "blog/post.html", context)

def add_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=True)
            return redirect(index)
        else:
            print(form.errors)
    else:
        form = PostForm()
    return render(request, "blog/add_post.html", {"form": form})