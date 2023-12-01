from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer


@api_view(['GET'])
def post_list_api (request):
    posts = Post.objects.all()
    data = PostSerializer(posts,many=True).data
    return Response({'data':data})


@api_view(['GET'])
def post_detail_api (request,pk):
    post = Post.objects.get(id=pk)
    data = PostSerializer(post).data
    return Response({'data':data})