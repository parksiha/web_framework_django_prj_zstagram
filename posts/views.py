from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from posts.models import Post, Comment
from posts.forms import CommentForm

# Create your views here.
def feeds(request):
    #로그인을 했다라면, 어떤 정보를 보내고,
    #로그인을 하지 않았다면, 로그인을 하도록 하자
    if not request.user.is_authenticated:
        return redirect('/users/login/') #redirect는 서버안에서 이루어짐, 빠르게 스위칭
    posts = Post.objects.all()
    comment_form = CommentForm()
    context = {
        "posts":posts,
        "comment_form": comment_form,
    }

    return render(request, 'posts/feeds.html', context)

@require_POST
def comment_add(request):
    form = CommentForm(data=request.POST)

    if form.is_valid():
        comment = form.save(commit=False)
        comment.comment = request.user

        comment.save()

        return redirect('/posts/feed_detail/', post_id=comment.post.id)

    return redirect("posts:feeds")


def feed_detail(request, post_id):
    if not request.user.is_authenticated:
        return redirect('/users/login/') #redirect는 서버안에서 이루어짐, 빠르게 스위칭
    post = Post.objects.get(id=post_id)
    comment_form = CommentForm()
    context = {
        "post":post,
        "comment_form": comment_form,
    }
    return render(request, 'posts/feed_detail.html', context)