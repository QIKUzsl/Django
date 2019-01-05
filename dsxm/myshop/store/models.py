# encoding: utf-8
# coding=utf-8
from django.db import models
from django.contrib.auth.models import User


class Store(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True, verbose_name="店铺名称")
    cover = models.ImageField(upload_to="static/images/public", default="static/images/public/default.png",
                              verbose_name="店铺头像")
    intro = models.TextField(verbose_name="店铺描述")
    openTime = models.DateField(auto_now_add=True, verbose_name="开店时间")
    status = models.ImageField(default=0, verbose_name="店铺状态")  # 0 正常1 暂停营业 2 永久删除
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="店铺所属")
