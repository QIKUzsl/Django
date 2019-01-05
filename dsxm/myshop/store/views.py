# encoding: utf-8
# coding=utf-8
from django.shortcuts import render, HttpResponse, redirect, reverse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from . import models
from django.views.decorators.http import require_GET
from goods.models import GoodsType, Goods


@login_required(login_url="/users/user_login/")
def add(request):
    if request.method == "GET":
        return render(request, "store/add.html", {})
    else:
        name = request.POST["name"]
        intro = request.POST["intro"]
        try:
            cover = request.FILRS["cover"]
            store = models.Store(name=name, intro=intro, cover=cover, user=request.user)
        except:
            store = models.Store(name=name, intro=intro, user=request.user)
        store.save()

        # return redirect(reverse("store:detail",kwargs={"s_id":store.id}))
        return redirect(reverse("store:list"))


@require_GET
@login_required
def list(request):
    stores = models.Store.objects.filter(user=request.user, status__in=[0, 1])
    return render(request, "store/list.html", {"stores": stores})


def detail(request, s_id):
    stores = models.Store.objects.filter(pk=s_id)
    type1 = GoodsType.objects.filter(parent__isnull=True)
    goods = Goods.objects.filter(store=stores)
    return render(request, "store/detail.html", {"stores": stores, "type1": type1, "goods": goods})


# def add(request):
#     pass


def update(request, s_id):
    pass


def change(request, s_id, status):
    store = models.Store.objects.get(id=s_id)
    store.status = status
    store.save()
    if store.status == 2:
        return redirect(reverse("store:list"))
    else:
        return render(request, "store/detail.html", {"store": store})


def store_base(req):
    return render(req, "store/store_base.html")
