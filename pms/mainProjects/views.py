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


# 搜索项目
def search_project(request):
    project_name = request.GET.get('project_name')
    project_id = request.GET.get('id')
    try:
        project_list = []
        if project_id:
            # 根据id搜索项目
            project = PmsMainProjectsList.objects.get(id=project_id)
            project_list.append({
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
        elif project_name:
            projects = PmsMainProjectsList.objects.filter(
                Q(project_name__exact=project_name) | Q(project_name__iexact=project_name))
            for project in projects:
                project_list.append({
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
        return JsonResponse({"code": 0, "msg": "查询项目成功", "projects": project_list})
    except Exception as e:
        return JsonResponse({
            'message': '项目不存在',
            'code': '1'
        }, status=404)


# 创建项目
@api_view(['POST'])
def create_product(request):
    reversed = request.POST
    project_name = reversed.get('project_name')
    project_base = reversed.get('project_base')
    project_num = reversed.get('project_num')
    project_owner = reversed.get('project_owner')
    project_resident = reversed.get('project_resident')
    project_product = reversed.get('project_product')
    project_update_time = reversed.get('project_update_time')
    project_update_user = reversed.get('project_update_user')
    project_update_file = reversed.get('project_update_file')
    project_ivc = reversed.get('project_ivc')
    project_db = reversed.get('project_db')
    project_middleware = reversed.get('project_middleware')

    # 如果传值为空，则使用默认值
    if not project_ivc:
        project_ivc = PmsMainProjectsList._meta.get_field('project_ivc').get_default()
    if not project_db:
        project_db = PmsMainProjectsList._meta.get_field('project_db').get_default()
    if not project_middleware:
        project_middleware = PmsMainProjectsList.meta.get_field('project_middleware'.get_default())
    try:
        # 检查项目是否已经存在
        if PmsMainProjectsList.objects.filter(project_num=project_num, project_name=project_name).exists():
            return JsonResponse({"code": 2, "msg": "该版本项目已存在，请勿重复创建"})
        # 创建项目
        product = PmsMainProjectsList.objects.create(project_name=project_name, project_base=project_base,
                                                     project_num=project_num, project_owner=project_owner,
                                                     project_resident=project_resident,
                                                     project_product=project_product,
                                                     project_update_time=project_update_time,
                                                     project_update_user=project_update_user,
                                                     project_update_file=project_update_file, project_ivc=project_ivc,
                                                     project_db=project_db,
                                                     project_middleware=project_middleware)
        return JsonResponse({"code": 0, "msg": "项目创建成功"})
    except Exception as e:
        print(e)
        return JsonResponse({"code": 1, "msg": "项目创建失败"})
