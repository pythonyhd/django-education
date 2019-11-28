# -*- coding: utf-8 -*-
# @Time    : 2019/11/27 15:57
# @Author  : King life
# @Email   : 18353626676@163.com
# @File    : urls.py
# @Software: PyCharm
from django.conf.urls import url, include
from .views import OrgView, AddUserAskView, OrgHomeView, OrgCourseView, OrgDescView, OrgTeacherView, AddFavView

# 新版本django必须指明app_name
app_name = 'organization'

urlpatterns = [
    # 授课机构首页
    url(r'^list/$', OrgView.as_view(), name='org_list'),
    # 列表表单url
    url(r'^add_ask/$', AddUserAskView.as_view(), name='add_ask'),
    url(r'^home/(?P<org_id>\d+)/$', OrgHomeView.as_view(), name='org_home'),
    # 机构课程详情页
    url(r'^course/(?P<org_id>\d+)/$', OrgCourseView.as_view(), name='org_course'),
    # 机构介绍页
    url(r'^desc/(?P<org_id>\d+)/$', OrgDescView.as_view(), name='org_desc'),
    # 讲师介绍页
    url(r'^teacher/(?P<org_id>\d+)/$', OrgTeacherView.as_view(), name='org_teacher'),
    # 机构收藏
    url(r'^add_fav/$', AddFavView.as_view(), name='add_fav'),
]