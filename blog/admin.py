from django.contrib import admin
from blog.models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at", "content", "tag", "image", "views")

# Register your models here.
admin.site.register(Post, PostAdmin)