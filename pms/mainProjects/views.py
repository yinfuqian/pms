from django.shortcuts import render
from django.db.models import Q
from django.http import JsonResponse
from rest_framework.decorators import api_view

from .models import PmsMainProjectsList
# Create your views here.
@api_view(['GET'])
# 所有列表
def projects_list(request):
    project = PmsMainProjectsList.objects.all()
    page_num = request.GET.get('pageNum')
    page_size = request.GET.get('pageSize')
    start = (int(page_num) - 1) * int(page_size)
    end = start + int(page_size)
    page_products = project[start:end]
    count = project.count()
    projects_list = []
    for project in page_products:
        projects_list.append({
            "id": project.id,
            "code": 0,
            "project_name": project.project_name,
            "project_base": project.project_base,
            "project_num": project.project_num,
            "project_owner": project.project_owner,
            "project_resident": project.project_resident,
            "project_product": project.project_product,
            "project_update_time": project.project_update_time,
            "project_update_user": project.project_update_user,
            "project_update_file": project.project_update_file,
            "project_ivc": project.project_ivc,
            "project_db": project.project_db,
            "project_middleware": project.project_middleware,
        })
    data = {
        'count': count,
    }
    return JsonResponse({"code": 0, "msg": "获取所有主线项目成功", "projects": projects_list, "pagination": data})
