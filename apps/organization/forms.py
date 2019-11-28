# -*- coding: utf-8 -*-
# @Time    : 2019/11/27 15:51
# @Author  : King life
# @Email   : 18353626676@163.com
# @File    : forms.py
# @Software: PyCharm
import re

from django import forms

from operation.models import UserAsk


# class UserAskForm(forms.Form):
#     name = forms.CharField(required=True, min_length=2, max_length=20)
#     mobile = forms.CharField(required=True, min_length=11, max_length=11)
#     course_name = forms.CharField(required=True, min_length=3, max_length=50)


class UserAskForm(forms.ModelForm):
    """
    表单验证
    """
    class Meta:
        model = UserAsk
        fields = ['name', 'mobile', 'course_name']

    def clean_mobile(self):
        """
        验证手机号
        :return:
        """
        mobile = self.cleaned_data['mobile']
        pattern = re.compile(r'^1[3456789]\d{9}$')
        if pattern.match(mobile):
            return mobile
        else:
            raise forms.ValidationError(u'手机号码不合法', code='mobile_invalid')