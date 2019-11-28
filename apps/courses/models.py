# -*- coding: utf-8 -*-
from datetime import datetime

from django.db import models

from organization.models import CourseOrg

# Create your models here.


class Course(models.Model):
    """课程表"""
    course_org = models.ForeignKey(CourseOrg, verbose_name=u'课程机构', null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, verbose_name=u'课程名称')
    desc = models.CharField(max_length=500, verbose_name=u'课程描述')
    detail = models.TextField(verbose_name=u'课程详情')
    degree = models.CharField(choices=(('cj', u'初级'), ('zj', u'中级'), ('gj', '高级')), max_length=10, verbose_name=u'课程难度')
    learn_times = models.IntegerField(default=0, verbose_name=u'学习时长')
    students = models.IntegerField(default=0, verbose_name=u'学习人数')
    fav_nums = models.IntegerField(default=0, verbose_name=u'收藏人数')
    image = models.ImageField(upload_to='course/%Y/%m', max_length=150, verbose_name=u'封面图')
    click_nums = models.IntegerField(default=0, verbose_name=u'点击量')  # 点击了不一定学习
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = '课程信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Lession(models.Model):
    """课程跟章节一对多关系，一个课对应多个章节"""
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name=u'课程')
    name = models.CharField(max_length=100, verbose_name=u'章节名')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = '章节'
        verbose_name_plural = verbose_name


class Video(models.Model):
    """视频名"""
    lesson = models.ForeignKey(Lession, on_delete=models.CASCADE, verbose_name=u'章节')
    name = models.CharField(max_length=100, verbose_name=u'视频名')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = '视频'
        verbose_name_plural = verbose_name


class CourseResource(models.Model):
    """视频来源"""
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name=u'课程')
    name = models.CharField(max_length=100, verbose_name=u'名称')
    download = models.FileField(upload_to='course/resource/%Y/%m', max_length=150, verbose_name=u'资源文件')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = '课程资源信息'
        verbose_name_plural = verbose_name