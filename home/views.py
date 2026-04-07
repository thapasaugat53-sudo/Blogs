from django.shortcuts import render, redirect

from .models import Post 
from .forms import CreatePost, EditPost

from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.
def homepage(request):
    posts = Post.objects.all()
    context = {
        "posts":posts
       
    }
    return render(request, 'home/homepage.html',context)

@login_required(login_url='login_user')
def getpost(request,id):
    post = Post.objects.get(id=id)

    context = {
        'post':post
    }
    return render (request, 'home/postdetail.html',context)

@login_required(login_url='login_user')
def createpost(request):
    form = CreatePost()
    if request.method == 'POST':
        user = request.user
        form = CreatePost(data=request.POST, files=request.FILES)
        if form.is_valid():
            Post = form.save(commit=False)
            Post.user = user
            Post.save()
        return redirect ('home')
    
    context = {
        'form':form,
    }
    return render(request, 'home/createpost.html',context)

@login_required(login_url='login_user')
def editpost(request,id):

    post = Post.objects.get(id=id)
    form = EditPost(instance=post)

    if request.method == 'POST':
        form = EditPost(data=request.POST, instance=post)
        if form.is_valid():
            form.save()
        return redirect ('home')    
    context = {
        'form':form,
    }
    return render(request, 'home/editpost.html',context)

@login_required(login_url='login_user')
def deletepost(request,id):
    post = Post.objects.get(id=id)
    post.delete()
    return redirect ('home')




def about(request):
    return render (request, 'home/about.html')




