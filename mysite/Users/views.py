from . import models
# 访问请求
from django.shortcuts import render
from django.shortcuts import HttpResponse
# 跨域装饰器
from django.views.decorators.csrf import csrf_exempt

# 重定向
from django.shortcuts import redirect, reverse

# 验证码
from io import BytesIO
from . import utlis
from django.conf import settings
# 邮箱验证
from django.core.mail import send_mail
from django.core.serializers import serialize
# ajax
from django.views.decorators.http import require_GET, require_POST
# 序列化
from django.http import JsonResponse

def index(request):
    return render(request, "index.html")

@csrf_exempt
def login(request):
    if request.method == "GET":
        return render(request, "Users/login.html", {})
    if request.method == "POST":
        username = request.POST['username'].strip()
        password = request.POST['password'].strip()
        pwd = utlis.hamcByMD5(password, settings.MD5_SALT)
        print(pwd)
        user = models.Users.objects.get(username=username)
        print(user)
        if user.count == 0:
            # 当用户密码输入错误次数达到三次的时候 进行重置密码
            return redirect(reverse("Users:update_login"))
        if user.count == 3:
            # count 加到三的时候清零
            user.count = 0
            user.save()
            return render(request, 'Users/login.html', {'msg': '密码输入超过3次，用户锁定十分钟'})
        if pwd != user.password:
            # 密码错误一次 count加一
            user.count += 1
            user.save()
            return render(request, "Users/login.html", {"msg": "密码错误"})

        try:
            user = models.Users.objects.get(username=username, password=pwd)
            # 登录成功后 保存状态
            request.session["loginUsers"] = user
            # 登录成功后重定向到首页面
            return redirect(reverse("Users:index"))
        except:
            return redirect(reverse("Users:login"))

# 登录忘记密码 进行修改密码
def update_login(request):
    if request.method == "GET":
        return render(request, "Users/logins.html")

@csrf_exempt
def register(request):
    if request.method == "GET":
        return render(request, "Users/register.html", {})
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        # 验证码
        code = request.POST.get('check_code')
        if code.upper() != request.session['CheckCode'].upper():
            return render(request, "Users/register.html", {"msg": "验证码错误"})
        if password != password2:
            return redirect(reverse("Users:register"), {"msg": "两次密码不同"})
        try:
            models.Users.objects.get(username=username)
            return render(request, "Users/register.html", {"msg", "已有用户，请重新注册"})
        except:
            # 进行加密
            pwd = utlis.hamcByMD5(password, settings.MD5_SALT)
            users = models.Users(username=username, email=email, password=pwd)
            users.save()
            # 基本资料填写完毕后跳转到补充资料页面 registers.html
            return render(request, "Users/registers.html", {})

# 注册详细资料
def add_register(request):
    if request.method == "POST":
        return redirect(reverse("Users:login"))

# ajax测试未成功
@require_GET
def register_ajax(request):
    username = request.GET["username"]
    user = models.Users.objects.filter(username=username)
    if user is not None:
        return JsonResponse({"msg": False})
    else:
        return JsonResponse({"msg": True})
# 验证码（2）
def check_code(request):
    stream = BytesIO()  # 开辟一块内存空间，不用写在外存，减少读写操作
    img, code = utlis.create_validate_code()
    img.save(stream, 'PNG')
    request.session['CheckCode'] = code
    return HttpResponse(stream.getvalue())

# 登出
def logout(request):
    # 退出的时候 删除用户登录信息
    del request.session["loginUsers"]
    return redirect(reverse("Users:index"))

# 验证码 暂时没用
@require_POST
def sends(request):
    qq = request.POST['qq']
    m_title = "赵电商账号激活邮件"
    m_msg = "点击激活您的账号"
    send_mail(m_title, m_msg, settings.EMAIL_FROM, [qq])
    return HttpResponse('发送成功')