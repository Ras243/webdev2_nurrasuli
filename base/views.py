from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from .models import Post

def home(request):
    posts = Post.objects.filter(active=True, featured=True)[:3]
    context = {'posts': posts}
    return render(request, 'base/index.html', context)

def posts(request):
    posts = Post.objects.filter(active=True, featured=True)
    context = {'posts': posts}
    return render(request, 'base/posts.html', context)

    # posts = [
    #     {
    #         'headline':'Laboratory Management System',
    #         'Sub_headline':'Designed built & mantained a the lab managment system for FOI Laboratories'
    #     },
    #     {
    #         'headline':'Online Store - Course',
    #         'Sub_headline':'Online store with paypal payments intergration and guest user shopping'
    #     },
    #     {
    #         'headline':'Membership Website',
    #         'Sub_headline':'Modulized guide for online courses with step by step intructions'
    #     },
        
    # ]

def post(request, pk):
    post = Post.objects.get(id=pk)
    context = {'post': post}
    return render(request, 'base/post.html', context)

def profile(request):
    return render(request, 'base/profile.html')

# VIEWS CRUD

@login_required(login_url="home")
def createPost(request):
    form = PostForm()

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('posts')
    
    context = {'form': form}
    return render(request, 'base/post_form.html', context)

@login_required(login_url="home")
def updatePost(request, pk):
    post = Post.objects.get(id=pk)
    form = PostForm(instance=post)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('posts')
 
    context = {'form': form}
    return render(request, 'base/post_form.html', context)

@login_required(login_url="home")
def deletePost(request, pk):
    post = Post.objects.get(id=pk)

    if request.method == 'POST':
        post.delete()
        return redirect('posts')
            
    context = {'item': post}
    return render(request, 'base/delete.html', context)


