# from mysite.seller.models import Seller
from . import models
# 访问请求
from django.shortcuts import render
from django.shortcuts import HttpResponse
# 跨域装饰器
from django.views.decorators.csrf import csrf_exempt

# 引入系统User表格
from django.contrib.auth.models import User

# 重定向
from django.shortcuts import redirect, reverse

# 验证码
from io import BytesIO
from . import utlis

from django.core.serializers import serialize
# ajax
from django.views.decorators.http import require_GET, require_POST
def index(request):
    return render(request, "index.html")

@csrf_exempt
def seller_login(request):
    if request.method == "GET":
        return render(request, "seller/seller_login.html", {})
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = models.Seller.objects.get(username=username, password=password)
            # 登录成功后 保存状态
            request.session["loginUsers"] = user
            # 登录成功后重定向到首页面
            return redirect(reverse("seller:seller_Center"))
        except:
            return render(request, "seller/seller_login.html")

@csrf_exempt
def seller_register(request):
    if request.method == "GET":
        return render(request, "seller/seller_register.html", {})
    if request.method == "POST":
        username = request.POST['username'].strip()
        password = request.POST['password'].strip()
        password2 = request.POST['password2'].strip()
        # 验证码
        code = request.POST.get('check_code')
        if code.upper() != request.session['CheckCode'].upper():
            return redirect(reverse("seller:seller_register"), {"msg": "验证码错误"})
        if password != password2:
            return redirect(reverse("seller:seller_register"), {"msg": "两次密码不同"})
        users = models.Seller(username=username, password=password,)
        users.save()
        return redirect(reverse("seller:seller_login"))


# 验证码（2）
def check_code(request):
    stream = BytesIO()  # 开辟一块内存空间，不用写在外存，减少读写操作
    img, code = utlis.create_validate_code()
    img.save(stream, 'PNG')
    request.session['CheckCode'] = code
    return HttpResponse(stream.getvalue())


def seller_logout(request):
    # 退出的时候 删除用户登录信息
    del request.session["loginUsers"]
    return redirect(reverse("seller:index"))


def seller_Center(request):
    return render(request, "seller/seller_Center.html")
