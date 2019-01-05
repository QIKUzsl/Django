from django.db import models
from tinymce.models import HTMLField

# Create your models here.


class Users(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50,verbose_name="用户名")
    age = models.IntegerField(verbose_name='年龄')
    passwd = models.CharField(max_length=225)

    def __str__(self):
        return self.name


class Article(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50,verbose_name='标题')
    # text = models.TextField(verbose_name='内容')
    content = HTMLField(verbose_name='内容')
    user = models.ForeignKey(Users, on_delete=models.CASCADE,verbose_name='作者')


class Login(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    passwd = models.CharField(max_length=225)
    header = models.FileField(upload_to="static/user/image",default='static/user/image/op.jpg')

    def __str__(self):
        return '%s,%s' % (self.username, self.passwd)