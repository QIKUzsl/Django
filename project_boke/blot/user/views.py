from django.shortcuts import render,redirect
from . import models
from io import BytesIO
from . import utils
from django.conf import settings
# Create your views here.
from django.http import HttpResponse



def home(req):
    return render(req, "user/home.html")

def login(req):
    if req.method == 'GET':
        return render(req, "user/login.html", {'msg': "请认真填写以下信息！！"})
    elif req.method == 'POST':
        name = req.POST['name']
        password = req.POST['passwd']
        passwd = utils.hashByMD5(password, settings.MD5_SALT)
        try:
            user = models.Login.objects.get(name=name, passwd=passwd)
            req.session['loginUser'] = user
            return redirect("user:home")
        except:
            return render(req, "user/login.html", {'msg':"用户名或密码错误！！"})



def createCode(req):
    f = BytesIO()
    img, code = utils.create_code()
    req.session['code'] = code
    img.save(f, 'PNG')
    print(code)
    return HttpResponse(f.getvalue())



def register(req):
    if req.method == 'GET':
        return render(req, "user/register.html", {'msg': "请认真填写以下信息！！"})
    elif req.method == 'POST':
        name = req.POST['name']
        passwd = req.POST['passwd']
        if len(name) > 6:
            if len(passwd) > 6:
                try:

                    models.Login.objects.get(name=name)
                    return render(req, "user/register.html", {'msg': "用户名已存在！！"})
                except:
                    try:
                        print("++++++++++++")
                        passwd = utils.hashByMD5(passwd, settings.MD5_SALT)
                        print("-----------------")
                        user = models.Login(name=name, passwd=passwd)
                        user.save()
                        return HttpResponse('注册成功！！')
                    except Exception as e:
                        print(e)
                        return render(req, "user/register.html", {'msg': "注册失败！！"})
            else:
                return render(req, "user/register.html",{'msg': "用户密码不能小于六位！！"})
        else:
            return render(req, "user/register.html",{'msg': "用户名称不能小于六位！！"})



def base(req):
    return render(req, "user/base.html")


def user_info(req):
    return render(req, "user/user_info.html")


def add_Article(req):
    if req.method == 'GET':
        return render(req, "user/add_Article.html")
    if req.method == 'POST':
        title = req.POST.get('title')
        content = req.POST.get('content')
        user_id = req.POST.get('user_id')
        Article = models.Article(title=title,content=content,user_id=user_id)
        Article.save()
        return HttpResponse("发表成功！！！")


# def Article_info(req):





















