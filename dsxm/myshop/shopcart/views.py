# encoding: utf-8
# coding=utf-8
from django.shortcuts import render, reverse, redirect
from django.views.decorators.http import require_GET
from django.contrib.auth.decorators import login_required
from goods.models import Goods, GoodsType
from . import models


@require_GET
@login_required
def add(request, count, goods_id):
    # goods = GoodsType.objects.get(pk=GoodsType_id)
    # good = Goods.objects.get(pk=goods_id)
    # user = request.user
    #
    # try:
    #     shopCart = models.ShopCart.objects.get(user=user, goods=goods, good=good)
    #     shopCart.count += int(count)
    #     shopCart.allTotal = shopCart.count * good.price
    #     shopCart.save()
    # except:
    #     shopCart = models.ShopCart(goods=goods, user=user, good=good)
    #     shopCart.count = int(count)
    #     shopCart.allTotal = shopCart.count * good.price
    #     shopCart.save()
    # return redirect(reverse("shopcart:list"))

    goods = Goods.objects.get(pk=goods_id)
    user = request.user

    try:
        shopCart = models.ShopCart.objects.get(user=user, goods=goods)
        shopCart.count += int(count)
        shopCart.allTotal = shopCart.count * goods.price
        shopCart.save()
    except:
        shopCart = models.ShopCart(goods=goods, user=user)
        shopCart.count = int(count)
        shopCart.allTotal = shopCart.count * goods.price
        shopCart.save()
    return redirect(reverse("shopcart:list"))


def list(request):
    shopcarts = models.ShopCart.objects.filter(user=request.user).order_by("-addTime")
    return render(request, "shopcart/list.html", {"shopcarts": shopcarts})


def drop(request):
    shopcarts = models.ShopCart.objects.filter(user=request.user).order_by("-addTime")
    shopcarts.delete()
    # return redirect("shopcart/list.html")
    return render(request, "shopcart/list.html", {"shopcarts": shopcarts})