# -*- coding: utf-8 -*-
# @Time    : 2019/11/25 17:40
# @Author  : King life
# @Email   : 18353626676@163.com
# @File    : adminx.py
# @Software: PyCharm
import xadmin
from xadmin import views
from users.models import EmailVerifyRecord, Banner


class BaseSetting(object):
    enable_themes = True  # 启用主题
    use_bootswatch = True


class GlobalSettings(object):
    site_title = '在线教育管理后台'  # 后台标题名称
    site_footer = '华氏集团'  # 底部显示名称
    menu_style = 'accordion'  # 把app进行收缩，点击可以展开


class EmailVerifyRecordAdmin(object):
    """
    xadmin注册邮箱后台
    """
    list_display = ['code', 'email', 'send_type', 'send_time']
    search_fields = ['code', 'email', 'send_type']
    list_filter = ['code', 'email', 'send_type', 'send_time']


class BannerAdmin(object):
    """
    xadmin注册轮播图后台
    """
    list_display = ['title', 'image', 'url', 'index', 'add_time']
    search_fields = ['title', 'image', 'url', 'index']
    list_filter = ['title', 'image', 'url', 'index', 'add_time']


xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)

xadmin.site.register(views.BaseAdminView, BaseSetting)  # 启用主题
xadmin.site.register(views.CommAdminView, GlobalSettings)  # 修改头跟底