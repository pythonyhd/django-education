# -*- coding: utf-8 -*-
from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class UserProfile(AbstractUser):
    """用户基本信息表"""
    nick_name = models.CharField(max_length=60, verbose_name=u'昵称', default="")
    birthday = models.DateField(verbose_name=u'生日', null=True, blank=True)
    gender = models.CharField(choices=(('male', u'男'), ('female', u'女')), max_length=8, default=u'')
    address = models.CharField(max_length=200, verbose_name=u'地址', default=u'')
    mobile = models.CharField(max_length=11, null=True, blank=True, verbose_name=u'手机号')
    image = models.ImageField(upload_to='images/%Y/%m', default=u'image/default.png', max_length=150, verbose_name=u'头像')

    class Meta:
        verbose_name = '用户基本信息'
        verbose_name_plural = verbose_name
        db_table = 'user_info'

    def __str__(self):
        return self.username


class EmailVerifyRecord(models.Model):
    """邮箱验证码"""
    code = models.CharField(max_length=20, verbose_name=u'验证码')
    email = models.EmailField(max_length=50, verbose_name=u'邮箱')
    send_type = models.CharField(choices=(('register', u'注册'), ('forget', u'找回密码')), max_length=20, verbose_name=u'选择类型')
    send_time = models.DateTimeField(default=datetime.now, verbose_name=u'发送时间')

    class Meta:
        verbose_name = '邮箱验证码'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.code


class Banner(models.Model):
    """轮播图"""
    title = models.CharField(max_length=150, verbose_name=u'标题')
    image = models.ImageField(upload_to='banner/%Y/%m', max_length=150, verbose_name=u'轮播图')
    url = models.URLField(max_length=200, verbose_name=u'详情链接')
    index = models.IntegerField(default=100, verbose_name=u'图片顺序')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = '轮播图'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title