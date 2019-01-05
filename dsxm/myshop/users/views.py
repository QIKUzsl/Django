# encoding: utf-8
# coding=utf-8
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.db import models
from users import models
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from . import utils
from io import BytesIO
from django.core.cache import cache
from django.conf import settings
from django.core.mail import send_mail
# from itsdangerous import TimedJSONWebSignatureSerializer as Serializer



def user_login(request):
    if request.method == "GET":
        try:
            next_url = request.GET['next']
        except:
            next_url = '/'
        print(next_url)
        return render(request, "users/login.html", {"next_url": next_url})
    elif request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        next_url = request.POST.get('next', '/')
        print(next_url)
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                code = request.POST.get('code')
                print(code)
                mycode = request.session['code']
                if code.upper() == mycode.upper():
                    # 将验证通过的信息保存在request,request.user.nickname取用户名称
                    login(request, user)
                    return render(request, "index.html")
                    # return redirect(next_url)
                else:

                    return render(request, "users/login.html", {'msg': '验证码不正确,请重新登录'})

            else:
                return render(request, "users/login.html", {"error_code": 2, "msg": "您的账号已被锁定，请联系管理员"})
        else:
            return render(request, "users/login.html", {"error_code": 3, "msg": "用户名称或密码错误，请重新登录"})


def updateUser(req):
    if req.method == "GET":
        # id = req.GET.get('user_id')
        # user = models.UserInfo.objects.get(id=id)
        return render(req, "users/updateUser.html")
    elif req.method == 'POST':
        id = req.POST.get('user_id')
        nickname = req.POST.get('nickname')
        age = req.POST.get('age')
        gender = req.POST.get('gender')
        phone = req.POST.get('phone')
        header = req.POST.get('header')
        user = models.UserInfo.objects.get(pk=id)
        cache.set('user', user)
        user.nickname = nickname
        user.age = age
        user.gender = gender
        user.phone = phone
        user.header = header
        user = cache.get('user')
        user.save()
        return redirect("users:userInfo")


def register(request):
    if request.method == "GET":
        return render(request, "users/register.html", {})
    elif request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        nickname = request.POST["nickname"]
        confirmpwd = request.POST["confirmpwd"]
        if password != confirmpwd:
            return render(request, "users/register.html", {"error_code": 1, "msg": "两次密码不一致，请重新输入"})
        try:
            User.objects.get(username=username)
            return render(request, "users/register.html", {"error_code": 2, "msg": "该用户名已存在，请重新输入"})
        except:

            try:
                models.UserInfo.objects.get(username=username)
                return render(request, "users/register.html", {"error_code": 3, "msg": "该用户昵称已存在，请重新输入"})
            except:
                user = User.objects.create_user(username=username, password=password)
                userInfo = models.UserInfo(nickname=nickname, user=user)
                user.save()
                userInfo.save()
                return render(request, "users/login.html", {"error_code": 1, "msg": "用户注册成功，请登录"})


@login_required()
def user_logout(request):
    logout(request)
    return render(request, "users/login.html", {"error_code": 4, "msg": "退出账号，请重新登录"})


# 验证码


def check_code(request):
    f = BytesIO()
    img, code = utils.create_code()
    request.session['code'] = code
    img.save(f, 'PNG')
    print(code)
    return HttpResponse(f.getvalue())


# 给验证码增加随机数
def createCode(request):
    f = BytesIO()
    img, code = utils.create_code()
    request.session['code'] = code
    img.save(f, 'PNG')
    print(code)
    return HttpResponse(f.getvalue())


@login_required(login_url="/users/user_login/")
def userInfo(request):
    return render(request, "users/userInfo.html")


def add_address(request):
    if request.method == "GET":
        return render(request, "users/add_address.html", {})
    else:
        recv_name = request.POST["recv_name"]
        recv_tel = request.POST["recv_tel"]
        province = request.POST["province"]
        city = request.POST["city"]
        area = request.POST["area"]
        street = request.POST["street"]
        desc = request.POST["desc"]
        try:
            is_default = request.POST["is_default"]
            addresses = models.Address.objects.filter(user=request.user)
            for address in addresses:
                address.is_default = False
                address.save()
            address = models.Address(recv_name=recv_name, recv_tel=recv_tel, province=province, city=city, area=area, \
                                     street=street, desc=desc, user=request.user, is_default=True)
            address.save()
        except:
            address = models.Address(recv_name=recv_name, recv_tel=recv_tel, province=province, city=city, area=area, \
                                     street=street, desc=desc, user=request.user)
            address.save()
        return redirect(reverse("users:add_address"))


def address_list(request):
    addresses = models.Address.objects.filter(user=request.user)
    return render(request, "users/address_list.html", {"addresses": addresses})
