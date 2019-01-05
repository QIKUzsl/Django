# encoding: utf-8
# coding=utf-8
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.views.decorators.http import require_GET
from . import models
from django.core.serializers import serialize
from store.models import Store


def add(request):
    if request.method == "GET":
        return render(request, "goods/add.html", {})
    else:
        name = request.POST["name"]
        price = request.POST['price']
        stock = request.POST["stock"]
        type2 = request.POST["type2"]
        intro = request.POST["intro"]
        cover = request.FILES["cover"]
        store_id = request.POST["store"]
        print("+++++++", store_id)

        #  可加验证
        # store_id = int(store_id)
        store = Store.objects.get(pk=store_id)
        goodsType = models.GoodsType.objects.get(pk=type2)
        goods = models.Goods(name=name, price=price, stock=stock, intro=intro, store=store, goodstype=goodsType)
        goods.save()
        goodImage = models.GoodsImage(path=cover, goods=goods)
        goodImage.save()
        # return redirect(reverse("index", kwargs={"s_id": store_id}))
        return redirect(reverse("store:detail", kwargs={"s_id": store_id}))


@require_GET
def findTypeByPid(request):
    parent_id = request.GET["parent_id"]
    type2s = models.GoodsType.objects.filter(parent=parent_id)
    print(type(type2s))
    return HttpResponse(serialize("json", type2s))

@require_GET
def detail(request, g_id):
    goods = models.Goods.objects.get(pk=g_id)
    return render(request, "goods/detail.html", {"goods": goods})
