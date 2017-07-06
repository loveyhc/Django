#coding=utf-8
from django.shortcuts import render, redirect
from models import UserInfo
from hashlib import sha1
from django.http import JsonResponse
# Create your views here.

def register(request):
    context = {'title':'注册'}
    return render(request, 'user/register.html',context)

def register_check2(request):
    uname = request.GET.get('uname')
    uname = UserInfo.objects.filter(uname=uname)
    if not uname:
        check = '0'
    else:
        check = '1'
    return JsonResponse({'check':check})

def register_check(request):
    post = request.POST
    uname = post.get('uname')
    upwd = post.get('upwd')
    email = post.get('email')

    s1 = sha1()
    s1.update(upwd)
    upwd_sha1 = s1.hexdigest()

    u = UserInfo()
    u.uname = uname
    u.upwd = upwd_sha1
    u.umail = email
    u.save()
    return redirect('/user/login/')

def login(request):
    #uname = request.COOKIES['uname']
    context = {'title':'登陆'}
    return render(request, 'user/login.html',context)

def login_check(request):
    post = request.POST
    uname = post.get('uname')
    upwd = post.get('upwd')
    ulist = UserInfo.objects.filter(uname=uname)

    if ulist: #二次判断，防止js被禁用
        s1 = sha1()
        s1.update(upwd)
        upwd_sha1 = s1.hexdigest()

        if ulist[0].upwd == upwd_sha1:
            request.session['uname'] = uname
            return redirect('/user/center_info/')
        else:
            return redirect('/user/login/')
    else:
        return redirect('/user/login/')

def login_check2(request): #ajax判断
    post = request.POST
    uname = post.get('uname')
    upwd = post.get('upwd')

    ulist = UserInfo.objects.filter(uname=uname)

    if ulist:
        s1 = sha1()
        s1.update(upwd)
        upwd_sha1 = s1.hexdigest()

        if ulist[0].upwd == upwd_sha1:
            return JsonResponse({'check': '2'})
        else:
            return JsonResponse({'check':'1'}) #密码错误

    else:
        return JsonResponse({'check':'0'}) #用户名不存在

def logout(request):
    request.session.flush()

def center_info(request):
    uname = request.session.get('uname')
    context = {'title': '用户中心', 'uname':uname, 'top':'1'}
    if uname:
        user = UserInfo.objects.filter(uname=uname)
        context['user'] = user[0]
    return render(request, 'user/user_center_info.html', context)

def center_order(request):
    pass

def center_site(request):
    pass

