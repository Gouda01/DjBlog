from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters



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


class PostListApi (generics.ListCreateAPIView) :
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    filterset_fields = ['author', 'draft']
    search_fields = ['title','content']
    ordering_fields = ['publish_date']


class PostDetailApi (generics.RetrieveUpdateDestroyAPIView) :
    queryset = Post.objects.all()
    serializer_class = PostSerializer