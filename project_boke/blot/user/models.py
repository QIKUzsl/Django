from django.db import models

# Create your models here.


class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255,verbose_name='用户名')


class Article(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=225, null=True)
    content = models.TextField()
    author = models.ForeignKey(User,on_delete=models.CASCADE)


class Login(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    passwd = models.CharField(max_length=255)
