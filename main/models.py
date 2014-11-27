#coding:utf-8
from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin

class Tag(models.Model):
    name = models.CharField(max_length=200, unique=True, verbose_name=u'名称')
    count_post = models.IntegerField(default=0, editable=False, verbose_name=u'文章数')
    def __unicode__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100,blank=True)
    intro = models.CharField(max_length=500,blank=True)
    content = models.TextField(max_length=99999)
    pub_date = models.DateTimeField(auto_now_add=True)
    website = models.URLField(blank=True)
    count_hit = models.IntegerField(default=0,editable=False, verbose_name=u'点击数')
    tags = models.ManyToManyField(Tag, blank=True, verbose_name=u'标签')
    def __unicode__(self):
        return self.title 
class Kola_message(models.Model):
    text = models.TextField(max_length=10000)
    name = models.CharField(max_length=100,blank=True)
    email = models.EmailField(blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return self.text
class Member(models.Model):
    name = models.CharField(max_length=50,blank=True)
    image = models.ImageField(upload_to='/static/photo/',blank=True)
    degree  = models.CharField(max_length=50,blank=True)
    intro = models.TextField(max_length=99999,blank=True)
    def __unicode__(self):
        return self.name

class Test(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100,blank=True)
    content = models.TextField(max_length=99999)
    def __unicode__(self):
        return self.title
class Center_user(models.Model):
    birthday = models.DateField(null=True,blank=True)
    img = models.ImageField(upload_to='photo',null=True,blank=True)
    big_img = models.ImageField(upload_to='photo',null=True,blank=True)
    small_img = models.ImageField(upload_to='photo',null=True,blank=True)
    phoneNum = models.CharField(max_length=13,null=True,blank=True)
    email = models.EmailField(null=True,blank=True)
    regTime = models.DateTimeField(null=True,blank=True)
    bio = models.TextField(null = True,blank=True)
    user = models.OneToOneField(User)
    def __unicode__(self):
        return self.bio
