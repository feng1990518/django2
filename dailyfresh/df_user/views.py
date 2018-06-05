from django.shortcuts import render, redirect
from hashlib import sha1
# Create your views here.
from .models import *



#注册页面
def register(request):
    return render(request,'df_user/register.html')


def register_handle(request):
    #接受用户输入
    post = request.POST
    uname = post.get('user_name')
    upwd = post.get('pwd')
    upwd2 = post.get('cpwd')
    uemail = post.get('email')
    #判断两次密码是否一致
    if upwd != upwd2:
        return redirect('/df_user/register/')
    #加密
    s1 = sha1()
    s1.update(upwd.encode('utf-8'))
    upwd3 = s1.hexdigest()

    #创建对象
    user = UserInfo()
    user.uname = uname
    user.upwd =upwd3
    user.uemail = uemail
    user.save()

    #注册成功后，跳转到首页
    return redirect('/df_user/login/')

