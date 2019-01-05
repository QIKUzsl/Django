from django.db import models
from django.conf import settings
import django.utils.timezone as timezone


class Users_registe(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=225)
    userpass = models.CharField(max_length=225)
    add_date = models.DateTimeField('注册日期',default = timezone.now,blank=None)
    mod_date = models.DateTimeField('最后修改日期', auto_now = True,blank=None)
    status = models.BooleanField(default=0)


class Users_Content(models.Model):
    id = models.AutoField(primary_key=True)
    nickname = models.CharField(max_length=225)
    age = models.IntegerField(max_length=225)
    gender = models.CharField(max_length=225)
    header = models.FileField()
    phone = models.CharField(max_length=225)
    email = models.CharField(max_length=225)
    Users_Content_id = models.ManyToManyField(Users_registe)


class Address(models.Model):
    id = models.AutoField(primary_key=True)
    recv_name = models.CharField(max_length=225)
    recv_phone = models.IntegerField(max_length=225)
    addre = models.CharField(max_length=225)
    desc = models.CharField(max_length=225)
    status = models.CharField(max_length=225)
    users_Address_id = models.ManyToManyField(Users_Content)


class GoodsType(models.Model):
    id = models.AutoField(primary_key=True)
