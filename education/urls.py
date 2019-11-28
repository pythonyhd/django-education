# -*- coding: utf-8 -*-
"""education URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.views.static import serve

import xadmin
from django.views.generic import TemplateView

from education.settings import MEDIA_ROOT
from users.views import LoginView, RegisterView, ActiveUserView, ForgetPwdView, ResetView, ModifyPwdView
from organization.views import OrgView

urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    url('^$', TemplateView.as_view(template_name='index.html'), name='index'),  # 主页
    # url('^login/$', TemplateView.as_view(template_name='login.html'), name='login'),  # 登录页
    url('^login/$', LoginView.as_view(), name='login'),  # 登录页
    url('^register/$', RegisterView.as_view(), name='register'),  # 注册页
    url(r'^captcha/', include('captcha.urls')),  # 验证码
    url(r'^active/(?P<active_code>.*)/$', ActiveUserView.as_view(), name='user_active'),  # 邮箱验证
    url(r'^forget/$', ForgetPwdView.as_view(), name='forget_pwd'),  # 忘记密码
    url(r'^reset/(?P<reset_code>.*)/$', ResetView.as_view(), name='reset_pwd'),  # 找回密码
    url(r'^modify_pwd/$', ModifyPwdView.as_view(), name='modify_pwd'),  # 找回密码表单

    # organization的url配置
    url(r'^org/', include('organization.urls', namespace='org')),
    # 处理media目录下的图片跟HTML页面相对应，上传文件的访问处理函数
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT})
]
