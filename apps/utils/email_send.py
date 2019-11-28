# -*- coding: utf-8 -*-
# @Time    : 2019/11/26 14:34
# @Author  : King life
# @Email   : 18353626676@163.com
# @File    : email_send.py
# @Software: PyCharm
from random import Random
from django.core.mail import send_mail

from users.models import EmailVerifyRecord
from education.settings import EMAIL_FROM


def random_str(randomlength=8):
    """
    生成随机字符串
    :return:
    """
    strs = ''
    chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        _idx = int(random.randint(0, length))
        strs += chars[_idx]
    return strs


def send_register_email(email, send_type='register'):
    email_record = EmailVerifyRecord()
    code = random_str(16)
    email_record.code = code
    email_record.email = email
    email_record.send_type = send_type
    email_record.save()

    email_title = ''
    email_body = ''

    if send_type == 'register':
        email_title = '注册激活网站链接'
        email_body = '请点击下面的链接激活账号:http://127.0.0.1:8000/active/{}'.format(code)

        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass
            # print('邮件发送成功')

    elif send_type == 'forget':
        email_title = '密码重置'
        email_body = '密码重置链接:http://127.0.0.1:8000/reset/{}'.format(code)

        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass