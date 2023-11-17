from django.shortcuts import render , redirect
from .models import Post
from django.views.generic import ListView , DetailView
from .forms import PostForm

# Create your views here.


def post_list (request):

    data = Post.objects.all()

    context = {
        'mahmoud' : data
    }
    return render(request,'posts/post_list.html',context)

def post_detail (request,post_id) :
    data = Post.objects.get(id = post_id)
    
    context = {
        'post' : data
    }
    return render (request , 'posts/post_detail.html' , context)


def create_post(request):
    if request.method == 'POST' :
        form = PostForm(request.POST,request.FILES)
        if form.is_valid() :
            form.save()
            return redirect ('/posts/')
    else :
        form = PostForm()

    return render (request,'posts/new.html',{'form':form})

def edit_post(request,pk):
    post = Post.objects.get(id=pk)

    if request.method == 'POST' :
        form = PostForm(request.POST,request.FILES,instance=post)
        if form.is_valid() :
            form.save()
            return redirect ('/posts/')
    else :
        form = PostForm(instance=post)

    return render (request,'posts/edit.html',{'form':form})


def delete_post(request,pk):
    post = Post.objects.get(id=pk)
    post.delete()
    return redirect ('/posts/')



class PostList (ListView) :
    model = Post

class PostDetail (DetailView):
    model = Post
