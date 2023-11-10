from django.shortcuts import render

from .models import Post

from django.views.generic import ListView , DetailView

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





class PostList (ListView) :
    model = Post

class PostDetail (DetailView):
    model = Post
