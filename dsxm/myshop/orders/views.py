# encoding: utf-8
# coding=utf-8
from django.shortcuts import render, reverse, redirect
from django.views.decorators.http import require_POST
from shopcart.models import ShopCart
from goods.models import Goods
from . import models
from users.models import Address


@require_POST
def confirm(request):
    g_ids = request.POST.getlist("g_id")
    print(g_ids)
    shopCarts = ShopCart.objects.filter(pk__in=g_ids)
    addresses = Address.objects.filter(user=request.user)
    print(addresses)
    return render(request, "orders/confirm.html", {"shopCarts": shopCarts, "addresses": addresses})


def pay(request):
    pass


@require_POST
def done(request):
    c_ids = request.POST.getlist("c_id")
    address_id = request.POST.get("address")

    address = Address.objects.get(pk=address_id)
    print(address.recv_name)
    shopcarts = ShopCart.objects.filter(pk__in=c_ids)

    addresses = address.province + "|" + address.city + "|" + address.area + "|" + address.street + "|" + address.desc

    order = models.Order(recvi_address=addresses, user=request.user, recvi_name=address.recv_name,
                         recvi_tel=address.recv_tel, all_price=0, remark="")
    order.save()
    allCount = 0

    for s in shopcarts:
        g = s.goods
        orderItem = models.OrderItem(good_id=g.id, goods_img=g.goodsimage_set.all().first().path, \
                                     goods_name=g.name, goods_price=g.price, goods_count=s.count, \
                                     goods_price_all=s.allTotal, order=order)
        orderItem.save()
        allCount += s.allTotal
    order.all_price = allCount
    order.save()
    return redirect(reverse("orders:list"))


def list(request):
    orders = models.Order.objects.filter(user=request.user)

    return render(request, "orders/list.html", {"orders": orders})


def detail(request):
    pass


def drop(request):
    orders = models.Order.objects.filter(user=request.user)
    orders.delete()
    return render(request, "orders/list.html", {"orders": orders})















