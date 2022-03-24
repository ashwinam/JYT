from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.
def blogHome(request):
    posts = Post.objects.all()
    context = {'posts':posts}
    return render(request, 'blog/blogHome.html', context)

def blogPost(request,slug):
    post = Post.objects.filter(slug=slug).first()
    context = {'post':post}
    return render(request, 'blog/blogPost.html', context)
    # return HttpResponse(f'<h1> this is blog post : {slug}</h1>')