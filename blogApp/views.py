from email import message
from multiprocessing import context
import re
from webbrowser import get
from django.contrib import messages
from django.shortcuts import redirect, render
from blogApp.forms import *
from blogApp.models import Blog, User
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.decorators import login_required
# list of all blogs
# @login_required
def list_blog(request):
    blogs=Blog.objects.all()
    context={"blogs":blogs}
    return render(request, 'index.html', context)

# @login_required
def blog_detail(request, id):
    get_blog = Blog.objects.get(id=id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid:
            comment = form.save(commit=False)
            comment.blog = get_blog
            comment.comment_by = request.user
            comment.save()

            return redirect('blog_detail', id=get_blog.id)
    else:
        form = CommentForm()
    return render(request, 'details.html', {'post': get_blog, 'form': form, })

@login_required
def add_blog(request):
    form=BlogForm()
    context={"form":form}
    if request.method == 'POST':
        blog_form=BlogForm(request.POST, request.FILES)
        if blog_form.is_valid():
           
            blog_form.save()
            return redirect('/')
        else:
            context={'form': blog_form}
            return render(request,'create_blog.html',context)
    return render(request,'create_blog.html',context)

@login_required
def update_items(request, pk):
    queryset= Blog.objects.get(id=pk)
    form = BlogForm(instance=queryset)
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES,instance=queryset )
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'form': form
    }
    return render(request, "update_blog.html", context)


# views for deleting a trainee
@login_required
def delete_items(request, pk):
    item = Blog.objects.get(id=pk)
    if request.user == item.author:
        item.delete()
        messages.success(request, 'successful deleted')
        return redirect('/')
        
    return render(request, "delete_blog.html")
# @login_required
# def delete_items(request, post_id):
#    item = Post.objects.get(pk=post_id)
#    if request.user == item.user:
#       Post.objects.filter(id=post_id).delete()
#       return redirect('posts:mypost')

# def signup(request):
#     form = UserRegistration()
#     if request.method == "POST":
#         form = UserRegistration(request.POST)  # UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('signin')
#         else:
#             form = UserRegistration()  # UserCreationForm()
#             return render(request, 'authentication/registration.html', {'form': form})
    
#     context = {'form': form }
#     return render(request, 'authentication/registration.html', context)

def signup(request):
    form=UserRegistration()
    context={
        'form':form
    }
    if request.method=="POST":
        form=UserRegistration(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signin')
        else:
            context={
                'form':form
            } 
    return render(request,'authentication/registration.html',context)

# user login
def log_user(request):
    # form = LoginForm()
    # context = {'form': form}
    if request.method == 'POST':
        # form = LoginForm(request.POST)
        username=request.POST.get('username')
        password=request.POST.get('password')   
        user=authenticate(request,username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('/')     
        else:
            messages.success(request, ("try again please ......"))
            return redirect('signin') 
            
    return render(request,'authentication/login.html') 


def signout(request):
    logout(request)
    return redirect('signin')