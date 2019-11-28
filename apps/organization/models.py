# -*- coding: utf-8 -*-
from datetime import datetime

from django.db import models

# Create your models here.


class CityDict(models.Model):
    """城市信息"""
    name = models.CharField(max_length=50, verbose_name=u'城市名')
    desc = models.CharField(max_length=200, verbose_name=u'城市描述')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = '城市'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class CourseOrg(models.Model):
    """课程机构基本信息"""
    name = models.CharField(max_length=50, verbose_name=u'机构名称')
    desc = models.TextField(max_length=500, verbose_name=u'机构描述')
    category = models.CharField(max_length=30, choices=(('pxjg', '培训机构'), ('gr', '个人'), ('gx', '高校')), verbose_name=u'机构类别', default='pxjg')
    click_nums = models.IntegerField(default=0, verbose_name=u'点击数')
    fav_nums = models.IntegerField(default=0, verbose_name=u'收藏数')
    # 再MySQL存储的相对路径地址，转换成url
    image = models.ImageField(upload_to='courseorg/%Y/%m', max_length=150, verbose_name=u'封面图')
    address = models.CharField(max_length=200, verbose_name=u'机构地址', default=u'')
    city = models.ForeignKey(CityDict, on_delete=models.CASCADE, verbose_name='所属城市')
    # 用于排序
    students = models.IntegerField(default=0, verbose_name=u'学习人数')
    course_nums = models.IntegerField(default=0, verbose_name=u'课程数')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = '机构信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Teacher(models.Model):
    """讲师信息"""
    org = models.ForeignKey(CourseOrg, on_delete=models.CASCADE, verbose_name=u'所属机构')
    name = models.CharField(max_length=50, verbose_name=u'讲师名称')
    work_years = models.IntegerField(default=0, verbose_name=u'工作年限')
    work_company = models.CharField(max_length=60, verbose_name=u'就职公司')
    work_position = models.CharField(max_length=30, verbose_name=u'公司职位')
    points = models.CharField(max_length=60, verbose_name=u'教学特点')
    click_nums = models.IntegerField(default=0, verbose_name=u'点击数')
    fav_nums = models.IntegerField(default=0, verbose_name=u'收藏数')
    image = models.ImageField(upload_to='teacher/%Y/%m', max_length=150, default='', verbose_name=u'教师封面')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = '讲师信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name