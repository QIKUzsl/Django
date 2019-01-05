# encoding: utf-8
# coding=utf-8
from django.shortcuts import render
from goods.models import GoodsType, Goods
from store import models
from store.views import detail


def index(request):
    # 第一个一级类型
    good_type1 = GoodsType.objects.filter(pk=10001)
    good_type1_2 = GoodsType.objects.filter(parent=good_type1)
    goods1_list = Goods.objects.filter(goodstype__in=good_type1_2)
    # 第二个一级类型
    good_type2 = GoodsType.objects.filter(pk=10002)
    good_type2_2 = GoodsType.objects.filter(parent=good_type2)
    goods2_list = Goods.objects.filter(goodstype__in=good_type2_2)
    allGoodsTypes = GoodsType.objects.filter(parent__isnull=True)

    return render(request, "index.html",
                  {"allGoodsType": allGoodsTypes, "goods1_list": goods1_list, "goods2_list": goods2_list})
