from email.policy import default
from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Categories(models.Model):
    name=models.CharField(max_length=50)
    thumb=models.ImageField(upload_to='categories', default=None)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name='category'
        verbose_name_plural='categories'

    
    def __str__(self):
        return self.name


class Articles(models.Model):
    title=models.CharField(max_length=100)
    subtitle=models.CharField(max_length=100)
    body=models.TextField()
    thumb=models.ImageField(upload_to='articles')
    author=models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    category=models.ManyToManyField(Categories)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name='article'
        verbose_name_plural='articles'


    def __str__(self):
        return self.title


    def snippet(self):
        return self.body[:40] + '...'

