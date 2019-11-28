# -*- coding: utf-8 -*-
# @Time    : 2019/11/25 18:37
# @Author  : King life
# @Email   : 18353626676@163.com
# @File    : adminx.py
# @Software: PyCharm
import xadmin
from courses.models import Course, Lession, Video, CourseResource


class CourseAdmin(object):
    """
    xadmin注册后台课程信息
    """
    list_display = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums', 'image', 'click_nums', 'add_time']
    search_fields = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums', 'image', 'click_nums']
    list_filter = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums', 'image', 'click_nums', 'add_time']


class LessionAdmin(object):
    """
    xadmin注册后台
    双下划线外键关联，进行对应的搜索
    """
    list_display = ['course', 'name', 'add_time']
    search_fields = ['course', 'name']
    list_filter = ['course__name', 'name', 'add_time']


class VideoAdmin(object):
    """注册视频信息"""
    list_display = ['lesson', 'name', 'add_time']
    search_fields = ['lesson', 'name']
    list_filter = ['lesson', 'name', 'add_time']


class CourseResourceAdmin(object):
    """详情推荐"""
    list_display = ['course', 'name', 'download', 'add_time']
    search_fields = ['course', 'name', 'download']
    list_filter = ['course', 'name', 'download', 'add_time']


xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Lession, LessionAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)