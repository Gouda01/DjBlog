from django.db import models
from django.utils import timezone
from taggit.managers import TaggableManager
from django.contrib.auth.models import User

# Create your models here.




class Post (models.Model):
    author = models.ForeignKey(User,related_name='post_author',on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=20000)
    draft = models.BooleanField(default=True)
    publish_date = models.DateTimeField(auto_now=True)
    #publish_date = models.DateTimeField(default=timezone.now)
    tags = TaggableManager()
    image = models.ImageField(upload_to='post')
    



    def __str__(self):
        return self.title