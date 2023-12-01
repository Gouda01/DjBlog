
from rest_framework import serializers
from .models import Post 
from django.contrib.auth.models import User


class AuthorSerializer (serializers.ModelSerializer) :
    class Meta :
        model = User
        fields = ['id','username','email']


class PostSerializer (serializers.ModelSerializer):
    author = AuthorSerializer()
    category = serializers.StringRelatedField()

    class Meta :
        model = Post
        fields = '__all__'