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




class PostList (ListView) :
    model = Post

class PostDetail (DetailView):
    model = Post
