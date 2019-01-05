from django.shortcuts import render,redirect
from django.template import loader
# Create your views here.
from django.http import HttpResponse
from . import models

temp1 = """
<html>
    <body style="text-align: center;">        
        <h1>查看所有可疑员</h1>
    </body>
</html>
"""
temp2 = """
<html>
    <body style="text-align: center;">        
        <h1>新增所有可疑员</h1>
    </body>
</html>
"""
temp3 = """
<html>
    <body style="text-align: center;">        
        <h1>删除所有可疑员</h1>
    </body>
</html>
"""


def findall(req):
    print(HttpResponse)
    print(dir(HttpResponse))
    print(req.method)
    print(req.GET)
    print(req.FILES)
    print(req.path)
    # print(dir(req))
    return HttpResponse(temp1)


def findgood(req):
    return HttpResponse(temp2)


def findbad(req):
    return HttpResponse(temp3)


# 增
# def create_user(req, username, passwd):
#     user = models.login.loginmanage.user_create(username, passwd)
#     return HttpResponse('注册成功')
#
#
# def login_get(req):
#     user = models.login.loginmanage.get()
#     # print(user)
#     return user


# 删除
def delete(req):
    user = models.Users(id=6, name="huasao", age=24)
    user.delete()
    return HttpResponse("删除成功")


# 改
# def update(req):
#     user = models.Users(id=6, name="huage", age=24)
#     user.save()
#     # user.update(id=6,name="huage",age=24)
#     return HttpResponse("更新成功")


def param(req, name):
    print(name)

    return HttpResponse("这个是使用位置参数方式")


def param1(req, name):
    print(name)
    return HttpResponse("这个是使用命名参数方式")
#
#
# def index(req):
#     name={'name':'zsl'}
#     user = models.Users.usermanage.get(pk=3)
#     users = models.Users.usermanage.all()
#     return render(req, "index.html",{"user":user,"name" :name['name'],"users":users})
#     # return render(req, "base.html",{"user":user,"name" :name['name'],"users":users})


def home(req):
    return render(req,"user/home.html")

def login(req):
    # print(req.GET)
    return render(req, "user/login.html")


# def register(req):
#     if req.method == "GET":
#         return render(req,"user/register.html",{'msg':'这是GET请求'})
#     else:
#     return render(req, "user/register.html")

#
# def login_success(req):
#     t = req.GET
#     username = t['username']
#     passwd = t['passwd']
#     try:
#         templates = models.login.loginmanage.get(username=username,passwd=passwd)
#         return render(req, "user/login_success.html")
#     except:
#         return render(req, "user/login_error.html")
#
#     # if not (username == templates.name and passwd == str(templates.password)):
#     #     return render(req, "user/login_error.html")
#     # else:
#     # return render(req, "user/login_success.html")
#     # templates = models.login.loginmanage.all()
#     # for u in templates:
#     #     name = u.username
#     #     password = u.passwd
#     #     if not (username == name and passwd == str(password)):
#     #         return render(req, "user/login_error.html")
#     #     else:
#     #         return render(req, "user/login_success.html")
#
#
# def text1(req):
#     return render(req, "user/text1.html")
#
#
# def register_success(req):
#     print(req.GET)
#     templates = req.GET
#     username = templates['username']
#     passwd = templates['passwd']
#     try:
#         templates = models.login.loginmanage.get(username=username,passwd=passwd)
#         return HttpResponse("用户名和密码已存在！！！！")
#     except:
#         return render(req, "user/register_success.html")
#     # create_user(req, username, passwd)
#
#     # return render(req, "user/register_success.html")
#
#
#
def update(req):
    return render(req,"update.html")
#
# def index1(req):
#     return render(req,"user/index1.html")
