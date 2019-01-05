# encoding: utf-8
# coding=utf-8
from django.db import models
from django.contrib.auth.models import User


class UserInfo(models.Model):
    id = models.AutoField(primary_key=True)
    # 用户昵称
    nickname = models.CharField(max_length=255, unique=True, verbose_name="用户昵称")
    # 用户年龄
    age = models.IntegerField(default=18, verbose_name="用户年龄")
    # 用户性别
    gender = models.CharField(max_length=10, default='男', verbose_name="用户性别")
    # 用户头像
    header = models.ImageField(upload_to="static/images/login", default="static/images/login/default.png",
                               verbose_name="用户头像")
    # 联系方式
    phone = models.CharField(max_length=55, verbose_name="用户电话号码")
    # 和系统内置的用户管理一对一表
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Address(models.Model):
    id = models.AutoField(primary_key=True)
    recv_name = models.CharField(max_length=100, verbose_name="收货人")
    recv_tel = models.CharField(max_length=20, verbose_name="收货人的电话号码")
    province = models.CharField(max_length=100, verbose_name="收货人的省份")
    city = models.CharField(max_length=100, verbose_name="收货人的城市")
    area = models.CharField(max_length=100, verbose_name="收货人的县区")
    street = models.CharField(max_length=100, verbose_name="收货人的街道")
    desc = models.CharField(max_length=100, verbose_name="详细地址")
    is_default = models.BooleanField(default=False, verbose_name="是否默认地址")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="地址所属用户")
