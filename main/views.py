#encoding:utf-8
from django.shortcuts import render_to_response,render,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect,Http404  
from django.core.paginator import Paginator,InvalidPage,EmptyPage,PageNotAnInteger
from main.models import *
from django.template import RequestContext,loader,Context
from django.contrib import auth
import random,os,re
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt

def index(req):
    list_blog = Blog.objects.all().order_by('pub_date').reverse()
    list_new=[]
    for i in range(9):
        list_new.append(list_blog[i])
    #list_new = list_blog[0:10]
    return render(req,'index.html',locals())
def about(req):
    return render(req,'about.html')
def download(req):
    list_file = Test.objects.all()
    return render(req,'download.html',locals())
def blog(req):
    mess = []
    messages_list = Kola_message.objects.order_by('-pub_date')[:10]
    blog_list = Blog.objects.order_by('-pub_date')
    paginator = Paginator(blog_list,10)
    page = req.GET.get('page')
    #meta = req.META
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        contacts = paginator.page(1)
    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)
    for i in messages_list:
            #留言板的标题和简介
        if len(i.text)>200:
            mess.append(i.text[:200]+'[...]')
        else:
            mess.append(i.text)
    messages = zip(messages_list,mess) 
    return render(req,'blog.html',locals())
    
def contact(req):
    list_test = Blog.objects.all().order_by('pub_date').reverse()
    return render(req,'contact.html',locals())
def user(req):
    return render(req,'user.html')
def gallery(req):
    return render(req,'gallery.html')
def detail(req,blog_id):
    '''
    详细博文内容
    '''
    try:
        blog = Blog.objects.get(pk=blog_id)
    except Blog.DoesNotExist:
        raise Http404
    return render(req,'blog-single.html',locals())
def test(req):
    test = Test.objects.all()
    return render_to_response('test.html',{"test":test})
def process_upload_file(request):
    # 获取文件
    #list_file = Test.objects.all()
    file_obj = request.FILES.get('your_file', None)
    if file_obj == None:
        return HttpResponse('file not existing in the request')
    # 写入文件
    file_name = file_obj.name
    #file_name = 'temp_我_file-%d' % random.randint(0,100000) # 不能使用文件名称，因为存在中文，会引起内部错误
    file_full_path = os.path.join('C:/upload_files/', file_name)
    #同步文件信息到数据库
    file_all = Test()
    file_title = re.finditer(r'C:/(upload_files/)(.*)',file_full_path)
    for i in file_title:
        file_all.author = i.group(2)
        file_all.title = i.group(1)+i.group(2)
    file_all.save()
    dest = open(file_full_path,'wb+')
    dest.write(file_obj.read())
    dest.close()
    return render_to_response('upload_result.html',{})
def register(request):
    errors=[]
    if request.method == 'POST':
        name = request.POST.get('username','')
        password1 = request.POST.get('password1','')
        password2 = request.POST.get('password2','')
        if len(name)<3:
            errors.append(u'用户名长度必须大于4个字符')
        elif len(password1)<6:
            errors.append(u'密码长度必须大于6个字符')
        elif password1 != password2 :
            errors.append(u'两次输入密码必须相同')
        else:
            try:
                user = User.objects.get(username=name)
                errors.append(u'用户名已被注册')
                return render(request,'register.html',{'errors':errors})
            except User.DoesNotExist:    
                user = User.objects.create_user(
                    username = name,
                    password = password1,
                    )
                register_flag = True
                return render(request,'login.html',{'register_flag':register_flag})
        return render(request,'register.html',{'errors':errors})
    else:
        return render(request,'register.html')
def login(request):
    errors = []
    register_flag = False
    if request.method == "POST":
        if not request.POST.get('username',''):
            errors.append(u"请输入用户名")
        if not request.POST.get('password',''):
            errors.append(u"请输入密码")
        else:
            name = request.POST.get('username','')
            password = request.POST.get('password','')
            user = auth.authenticate(username=name,
                password=password)
            if user is not None and user.is_active:
                auth.login(request,user)
                return HttpResponseRedirect("/index/")
            else:
                errors.append(u'登录失败，请重试')
    #response = render(request,'login.html',locals())
    response = render_to_response('login.html',
        {'errors':errors,},
        context_instance=RequestContext(request))
    return render(request,'login.html',locals())
def logout(request):
    if request.user.is_authenticated():
        auth.logout(request)
        return render(request,"logout.html",{})
    else:
#        return render(request,"logout.html",{})
        return HttpResponseRedirect("/index/") 
