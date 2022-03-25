from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import messages
from blog.templatetags import extras
from .models import BlogComment, Post

# Create your views here.
def blogHome(request):
    posts = Post.objects.all()
    context = {'posts':posts}
    return render(request, 'blog/blogHome.html', context)

def blogPost(request,slug):
    post = Post.objects.filter(slug=slug).first()
    comment = BlogComment.objects.filter(post=post, parent=None)
    replies = BlogComment.objects.filter(post=post).exclude(parent=None)
    replyDict = {}
    for reply in replies:
        if reply.parent.id not in replyDict.keys():
            replyDict[reply.parent.id]=[reply]
        else:
            replyDict[reply.parent.id].append(reply)
    context = {'post':post, 'comments':comment, 'replyDict':replyDict}
    return render(request, 'blog/blogPost.html', context)


def post_comment(request):
    if request.method == 'POST':
        comment = request.POST.get("comment")
        user = request.user
        post_sno = request.POST.get("post_sno")
        post = Post.objects.get(id=post_sno)
        parent_sno = request.POST.get("parent_sno")
        if parent_sno == "":
            comment = BlogComment(comment=comment, user=user, post=post)
            comment.save()
            messages.success(request, "Your Comment has been Posted Successfully")
        else:
            parent = BlogComment.objects.get(id=parent_sno)
            comment = BlogComment(comment=comment, user=user, post=post, parent=parent)
            comment.save()
            messages.success(request, "Your Reply has been Posted Successfully")
    return redirect(f"/blog/{post.slug}")