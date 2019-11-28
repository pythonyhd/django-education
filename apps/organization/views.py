# -*- coding: utf-8 -*-
import json

from django.shortcuts import render
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
from django.views.generic.base import View
from django.http import HttpResponse

from organization.forms import UserAskForm
from .models import CourseOrg, CityDict


class OrgView(View):
    """
    课程机构列表功能
    """
    def get(self, request):
        # 课程机构
        all_orgs = CourseOrg.objects.all()
        # 授课机构排名
        hot_orgs = all_orgs.order_by('-click_nums')[:3]
        # 城市名
        all_citys = CityDict.objects.all()
        # 取出根据城市筛选
        city_id = request.GET.get('city', '')
        if city_id:
            all_orgs = all_orgs.filter(city_id=int(city_id))
        # 排序功能
        sort = request.GET.get('sort', '')
        if sort:
            # 学习人数排名
            if sort == 'students':
                all_orgs = all_orgs.order_by('-students')
            elif sort == 'courses':
                all_orgs = all_orgs.order_by('-course_nums')
        # 类别筛选
        category = request.GET.get('ct', '')
        if category:
            all_orgs = all_orgs.filter(category=category)
        # 数目统计
        org_nums = all_orgs.count()
        # 分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        # Provide Paginator with the request object for complete querystring generation
        p = Paginator(all_orgs, 5, request=request)
        orgs = p.page(page)
        return render(request, 'org-list.html', {
            'all_orgs': orgs,
            'all_citys': all_citys,
            'org_nums': org_nums,
            'city_id': city_id,
            'category': category,
            'hot_orgs': hot_orgs,
            'sort': sort,
        })


class AddUserAskView(View):
    """
    用户添加咨询
    """
    def post(self, request):
        userask_form = UserAskForm(request.POST)
        if userask_form.is_valid():
            user_ask = userask_form.save(commit=True)
            # 异步操作，不进行页面跳转，返回json
            return HttpResponse(json.dumps({'status': 'success'}), content_type='application/json')
        else:
            return HttpResponse(json.dumps({'status': 'fail', 'msg': "{}".format(userask_form.errors)}), content_type='application/json')


class OrgHomeView(View):
    """
    机构首页详情页
    """
    def get(self, request, org_id):
        course_org = CourseOrg.objects.get(id=int(org_id))
        all_courses = course_org.course_set.all()[:3]  # 根据外键取值
        all_teachers = course_org.teacher_set.all()[:1]

        return render(request, 'org-detail-homepage.html', {
            'all_courses': all_courses,
            'all_teachers': all_teachers,
            'course_org': course_org,
        })