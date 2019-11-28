# -*- coding: utf-8 -*-
# @Time    : 2019/11/27 15:57
# @Author  : King life
# @Email   : 18353626676@163.com
# @File    : urls.py
# @Software: PyCharm
from django.conf.urls import url, include
from .views import OrgView, AddUserAskView, OrgHomeView

# 新版本django必须指明app_name
app_name = 'organization'

urlpatterns = [
    # 授课机构首页
    url(r'^list/$', OrgView.as_view(), name='org_list'),
    # 列表表单url
    url(r'^add_ask/$', AddUserAskView.as_view(), name='add_ask'),
    url(r'^home/(?P<org_id>\d+)/$', OrgHomeView.as_view(), name='org_home'),
]