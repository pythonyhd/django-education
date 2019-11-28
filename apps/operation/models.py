# -*- coding: utf-8 -*-
from datetime import datetime

from django.db import models

from users.models import UserProfile
from courses.models import Course
# Create your models here.


class UserAsk(models.Model):
    """用户提问"""
    name = models.CharField(max_length=50, verbose_name=u'姓名')
    mobile = models.CharField(max_length=11, verbose_name=u'电话')
    course_name = models.CharField(max_length=50, verbose_name=u'课程名')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = '用户咨询'
        verbose_name_plural = verbose_name


class CourseComments(models.Model):
    """评论信息"""
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name=u'用户信息')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name=u'课程信息')
    comments = models.CharField(max_length=300, verbose_name=u'评论信息')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = '课程评论'
        verbose_name_plural = verbose_name


class UserFavorite(models.Model):
    """用户收藏"""
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name=u'用户信息')
    fav_id = models.IntegerField(verbose_name=u'id标识')  # 用户收藏的是课程，机构还是老师
    fav_type = models.IntegerField(choices=((1, '课程'), (2, '机构'), (3, '讲师')), default=1, verbose_name=u'收藏类型')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = '用户收藏'
        verbose_name_plural = verbose_name


class UserMessage(models.Model):
    """用户消息"""
    user = models.IntegerField(default=0, verbose_name=u'接收用户')
    message = models.CharField(max_length=500, verbose_name=u'消息内容')
    has_read = models.BooleanField(default=u'未读', verbose_name=u'是否已读')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = '用户消息'
        verbose_name_plural = verbose_name


class UserCourse(models.Model):
    """记录用户课程"""
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name=u'用户信息')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name=u'课程信息')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = '用户课程'
        verbose_name_plural = verbose_name
