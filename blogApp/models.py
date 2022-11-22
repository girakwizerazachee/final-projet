from multiprocessing.sharedctypes import Value
from django.db import models

# Create your models here.
from django.db import models
import uuid
from django.contrib.auth import get_user_model

# Create your models here.
User=get_user_model()
class Blog(models.Model):
    id=models.UUIDField(default=uuid.uuid4,primary_key=True,editable=False)
    title = models.CharField(max_length=100, blank=False)
    type=models.CharField(max_length=200)
    headings = models.CharField(max_length=100, blank=False)
    poster = models.ImageField(upload_to="images/", null=True)
    content = models.TextField(blank=False)
    author = models.ForeignKey(User, on_delete= models.CASCADE, related_name="authors_blogs")
    slug = models.CharField(max_length=255,)
    created_on = models.DateTimeField(auto_now_add=True)
    "instance.get_total_likes()"
    "instance.get_total_likes"
    @property
    def get_total_likes(self):
        return self.blog_likes__count()
    def __str__(self):
        return str(self.title)
    def get_permission(self):
        pass
class BlogLikes(models.Model):
    id=models.UUIDField(default=uuid.uuid4,primary_key=True,editable=False)
    users=models.ManyToManyField(User,related_name="likees")
    blog=models.OneToOneField(Blog, related_name="blog_likes", on_delete=models.CASCADE)
    created_on=models.DateTimeField(auto_now_add=True)
    
    
class Comment(models.Model):
    id=models.UUIDField(default=uuid.uuid4,primary_key=True,editable=False)
    blog=models.ForeignKey(Blog,related_name="blog_comment",on_delete=models.CASCADE)
    comment_by=models.ForeignKey(User,related_name="user_comment",on_delete=models.CASCADE)
    comment_content=models.TextField()
    created_on=models.DateTimeField(auto_now_add=True)