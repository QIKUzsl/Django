from django.db import models


class Users(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    age = models.IntegerField()


class Article(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    text = models.TextField()
    user = models.ForeignKey(Users, on_delete=models.CASCADE)


class login(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    passwd = models.IntegerField()
    avatar = models.FileField(upload_to='static/user/image')
