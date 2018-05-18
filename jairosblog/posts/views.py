from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.
def home(request):
    posts = Post.objects.order_by('-pub_date') # - reverses order of posts.
    return render(request, 'posts/home.html', {'posts': posts})

def post_detail(request, post_id):
    #post = Post.objects.get(pk=post_id)
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'posts/post_detail.html', {'post_id': post_id, 'post': post})
