from django.shortcuts import render,redirect
from . import models
from . import utils
from . import form
from io import BytesIO
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from django.http import HttpResponse
from django.forms.models import model_to_dict
from django.core.serializers import serialize
from django.contrib.auth.decorators import login_required
from django.core.cache import cache
from django.core.paginator import Paginator


def home(req):
    PAGESIZE = 2
    user = models.Login.objects.all()
    paginator = Paginator(user, PAGESIZE)
    pageNow = req.GET.get('pageNow',default=1)
    page = paginator.page(pageNow)
    # print(PAGESIZE)
    # print(len(user))
    return render(req,"user/home.html",{'page':page,'paginator':paginator})


def register(req):
    if req.method == "GET":
        return render(req,"user/register.html")
    elif req.method == "POST":
        name=req.POST.get('username')
        passwd = req.POST.get('passwd')
        try:
            avatar = req.FILES.get('header')
            if avatar is null:
                user = models.Login(username=name, passwd=passwd)
                user.save()
            else:
                user = models.Login(username=name, passwd=passwd, header=avatar)
                user.save()
        except:
            user = models.Login(username=name, passwd=passwd)
            user.save()
        return render(req,"user/register_success.html")


def login(req):
    if req.method == "GET":
        return render(req,"user/login.html")
    elif req.method == "POST":
        username=req.POST.get('username')
        passwd = req.POST.get('passwd')
        try:
            code = req.POST.get('code')
            print(code)
            mycode = req.session['code']
            temp = models.Login.objects.get(username=username, passwd=passwd)
            req.session['loginUser']=temp
            if code.upper() == mycode.upper():
                return render(req,"user/login_success.html")
            else:
                msg = {'msg':'验证码不正确'}
                return render(req,"user/login.html", msg)
        except Exception as e:
            print("-----",e)
            return redirect("user:home")


def text1(req):
    return render(req,"user/text1.html")


def list_users(req):
    user = cache.get('user')
    if user is None:
        user = models.Login.objects.all()
        cache.set('user', user)
    return render(req, "user/list_users.html", {'user': user})


def updateUser(req):
    if req.method == "GET":
        id = req.GET.get('sid')
        user = models.Login.objects.get(id=id)
        return render(req, "user/updateUser.html", {'user': user})
    elif req.method == 'POST':
        id = req.POST.get('sid')
        name = req.POST.get('username')
        passwd = req.POST.get('passwd')
        avatar = req.POST.get('avatar')
        user = models.Login.objects.get(pk=id)
        cache.set('user', user)
        user.username = name
        user.passwd = passwd
        user.avatar = avatar
        user = cache.get('user')
        user.save()
        return redirect("user:list_users")


def delUser(req):
    id = req.GET.get('sid')
    user=models.Login.objects.get(pk=id)
    user.delete()
    return redirect("user:list_users")


def addArcticle(req):
    if req.method == "GET":
        return render(req, "user/addArcticle.html")
    elif req.method == "POST":
        print('++++++++++++++++++++++++')
        title = req.POST.get("title")
        print(title)
        content = req.POST.get("content")
        user_id = req.POST.get("user_id")
        user = models.Article(title=title, content=content, user_id=user_id)

        user.save()
        return redirect("user:list_article")

# @csrf_exempt
# def addArcticle_ajax(req):
#     if req.method == "GET":
#         return render(req, "user/addArcticle_ajax.html")
#     elif req.method == "POST":
#         print('++++++++++++++++++++++++')
#         title = req.POST.get("title")
#         print(title)
#         content = req.POST.get("content")
#         user_id = req.POST.get("user_id")
#         user = models.Article(title=title, content=content, user_id=user_id)
#
#         user.save()
#         return redirect("user:list_article")


def list_article(req):
    article = models.Article.objects.all()
    return render(req,'user/list_article.html',{"article":article})


def createCode(req):
    f = BytesIO()
    img,code = utils.create_code()
    req.session['code'] = code
    img.save(f,'PNG')
    print(code)
    return HttpResponse(f.getvalue())




@csrf_exempt
def text(req):
    if req.method == "GET":
        return render(req,'user/text.html')
    elif req.method == "POST":
        users = models.Login.objects.all()
        users = serialize('json',users)
        return HttpResponse(users)



from django.db import transaction


def rep(req):
    u = transaction.savepoint()
    try:
        user = models.Login(username="zsl",passwd="22")
        user.save()
        user = models.Users(name="zsl",age=43,passwd=123456)
        user.save()
        transaction.commit(u)
        return HttpResponse("OK!!!")
    except:
        transaction.rollback(u)
        return HttpResponse("SORRY!!!")



def register1(req):
    form1 = form.Userform()
    if req.method == "GET":
        return render(req,"user/register1.html",{'form1':form1})
    elif req.method == "POST":
        form1 = form.Userform(req.POST)
        print(form1.data.get('name'))
        return render(req,"user/login.html",{'msg':'测试'})

