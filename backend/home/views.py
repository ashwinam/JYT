from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact
from django.contrib import messages
from blog.models import Post

# Create your views here.

def home(request):
    return render(request, 'home/home.html')

def about(request):
    return render(request, 'home/about.html')
    # return HttpResponse('This is about Page')
    
def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone  = request.POST['phone']
        content = request.POST['content']
        if len(name) < 2 or len(email) < 3 or len(phone) < 10 or len(content) < 4:
            messages.error(request, "please fill the form correctly") 
        else:
            contact = Contact(name=name, email=email, phone=phone, content=content)
            contact.save()
            messages.success(request, "Your message suuccessfully sent")
        
    return render(request, 'home/contact.html')
    # return HttpResponse('This is Contact page')

def search(request):
    query = request.GET['search']
    if len(query) > 50:
        search_post = Post.objects.none()
    else:
        search_post_title = Post.objects.filter(title__icontains=query)
        search_post_content = Post.objects.filter(content__icontains=query)
        search_post = search_post_title.union(search_post_content)
    
    if search_post.count() == 0:
        messages.warning(request, "No search Result Found. Please Refine Your query.")
    context = {'posts':search_post, 'query':query}
    return render(request, 'home/search.html', context)