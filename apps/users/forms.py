# -*- coding: utf-8 -*-
# @Time    : 2019/11/26 11:28
# @Author  : King life
# @Email   : 18353626676@163.com
# @File    : forms.py
# @Software: PyCharm
from django import forms
from captcha.fields import CaptchaField


class LoginForm(forms.Form):
    """
    登录验证
    """
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=3)


class RegisterForm(forms.Form):
    """
    邮箱注册
    """
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, min_length=3)
    # myfield = AnyOtherField()
    captcha = CaptchaField(error_messages={'invalid': '验证码错误'})


class ForgetForm(forms.Form):
    """
    忘记密码验证
    """
    email = forms.EmailField(required=True)
    captcha = CaptchaField(error_messages={'invalid': '验证码错误'})


class ModifyPwdForm(forms.Form):
    """
    修改密码
    """
    password1 = forms.CharField(required=True, min_length=3)
    password2 = forms.CharField(required=True, min_length=3)