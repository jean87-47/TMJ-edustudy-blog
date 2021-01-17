from django.db import models
from django.conf import settings

class Category(models.Model):
    name = models.CharField(max_length=20, null=False)

    def __str__(self):
        return self.name

class Post(models.Model):
    title=models.CharField(max_length=140,blank=True)
    image=models.ImageField(blank=True)
    content=models.TextField()
    category = models.ForeignKey(Category, null=False, on_delete=models.CASCADE)
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,blank=True,null=True)
    link = models.URLField(null=True,blank=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    content=models.TextField()
    image=models.ImageField(blank=True)
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    created_date=models.DateTimeField(auto_now_add=True)
    link = models.URLField(null=True, blank=True)

    def __str__(self):
        a = '에 대한 답변'
        return self.post.title + a



class Key(models.Model):
    key_number=models.CharField(max_length=140)

