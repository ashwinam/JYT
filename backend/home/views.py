from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
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

def signUpHandler(request):
    if request.method=='POST':
        username = request.POST['username']
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        # checks
        # 1. Length of username must Be 10 character long
        if len(username) > 10:
            messages.error(request, "Username Must be Under 10 characters ")
            return redirect('home')

        # 2. username should be alphanumeric
        if username.isalnum():
            messages.error(request, "Username should only contain letters and numbers")
            return redirect('home')

        # 3. both password fields should be match
        if pass1 != pass2:
            messages.error(request, "Passwords Do not match")
            return redirect('home')

        my_user = User.objects.create_user(username, email, pass1)
        my_user.first_name=first_name
        my_user.last_name=last_name
        my_user.save()
        messages.success(request, "Your JYT account has been successfully created")
        return redirect('home')
    else:
        return HttpResponse("404 Not Found")

def loginHandler(request):
    if request.method == 'POST':
        login_username = request.POST['login_username']
        login_password = request.POST['login_password']

        user = authenticate(username=login_username, password=login_password)

        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect('home')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('home')
    else:
        return HttpResponse("404 Not Found")

def logoutHandler(request):
    logout(request)
    messages.success(request, "successfully Logged Out")
    return redirect('home')