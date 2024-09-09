from django.shortcuts import render, get_object_or_404
from .models import Post


def renderPosts(request):
    total_posts = Post.objects.count()
    posts = Post.objects.order_by("-date")
    context = {
        "title": "Blog",
        "total_posts": total_posts,
        "posts": posts, "total_posts": total_posts,
    }
    return render(request, "blog.html", context)


def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    context = {
        "title": post.title,
        "post": post,
    }
    return render(request, "post_detail.html", context)
