# Create your views here.
import datetime

from django.http import JsonResponse
from django.views.decorators.http import require_POST
from rest_framework.decorators import api_view
from django.db.models import Q
from .models import PmsOperationLogs


# 记录操作

@require_POST
def record_user_operation(request):
    time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    if request.POST.get('project_name') and request.POST.get('file_name'):
        try:
            # 获取当前登录用户
            if request.POST.get('file_name') == "undefined":
                file_name = "未作变动"
            else:
                file_name = request.POST.get('file_name')
            user = request.POST.get('user')
            content = request.POST.get('content')
            operation_type = request.POST.get('operation_type')
            project_name = request.POST.get('project_name')
            # 记录用户操作历史

            operation_history = PmsOperationLogs(
                file_name=file_name,
                project_name=project_name,
                user=user,
                content=content,
                operation_type=operation_type,
                timestamp=time  # 添加时间戳
            )
            operation_history.save()
            return JsonResponse({'message': '操作历史记录成功'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    # elif request.POST.get('project_name'):
    #     try:
    #         # 获取当前登录用户
    #         project_name = request.POST.get('project_name')
    #         user = request.POST.get('user')
    #         content = request.POST.get('content')
    #         operation_type = request.POST.get('operation_type')
    #         # 记录用户操作历史
    #         operation_history = PmsOperationLogs(
    #             project_name=project_name,
    #             user=user,
    #             content=content,
    #             operation_type=operation_type,
    #             timestamp=datetime.datetime.now()  # 添加时间戳
    #         )
    #         operation_history.save()
    #         return JsonResponse({'message': '操作历史记录成功'})
    #     except Exception as e:
    #         return JsonResponse({'error': str(e)}, status=500)
    else:
        try:
            # 获取当前登录用户
            user = request.POST.get('user')
            content = request.POST.get('content')
            operation_type = request.POST.get('operation_type')

            # 记录用户操作历史
            print(time)
            operation_history = PmsOperationLogs(
                user=user,
                content=content,
                operation_type=operation_type,
                timestamp=time  # 添加时间戳
            )
            operation_history.save()
            return JsonResponse({'message': '操作历史记录成功'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)


# 查询所有操作
@api_view(['GET'])
# 所有列表
def operations_list(request):
    operations = PmsOperationLogs.objects.all()
    page_num = request.GET.get('pageNum')
    page_size = request.GET.get('pageSize')
    if not page_num or not page_size:
        operations_list = []
        for operation in operations:
            if operation.project_name and operation.file_name:
                formatted_content = f"{operation.content}项目名称:{operation.project_name}文件名称:{operation.file_name}"
            elif operation.project_name and not operation.file_name:
                formatted_content = f"{operation.content}项目名称:{operation.project_name}"
            else:
                formatted_content = f"{operation.content}"
            operations_list.append({
                "id": operation.id,
                "user": operation.user,
                "code": 0,
                "timestamp": operation.timestamp,
                "formatted_content": formatted_content})
        data = len(operations_list)
    else:
        start = (int(page_num) - 1) * int(page_size)
        end = start + int(page_size)
        page_operation = operations[start:end]
        count = operations.count()
        operations_list = []
        for operation in page_operation:
            if operation.project_name and operation.file_name:
                formatted_content = f"{operation.content}项目名称:{operation.project_name}文件名称:{operation.file_name}"
            elif operation.project_name and not operation.file_name:
                formatted_content = f"{operation.content}项目名称:{operation.project_name}"
            else:
                formatted_content = f"{operation.content}"
            operations_list.append({
                "id": operation.id,
                "code": 0,
                "user": operation.user,
                "timestamp": operation.timestamp,
                "formatted_content": formatted_content})
        data = {
            'count': count,
        }
    return JsonResponse({"code": 0, "msg": "获取所有操作日志成功", "operations": operations_list, "pagination": data})


# 搜索
def operations_search(request):
    search_query = request.GET.get('search_query', '')
    operations_list = []
    operations = PmsOperationLogs.objects.filter(
        Q(user__icontains=search_query) |  # 匹配 user 字段
        Q(content__icontains=search_query) |  # 匹配 content 字段
        Q(project_name__icontains=search_query) |  # 匹配 project_name 字段
        Q(file_name__icontains=search_query)  # 匹配 file_name 字段
    )
    for operation in operations:
        if operation.project_name and operation.file_name:
            formatted_content = f"{operation.content}项目名称:{operation.project_name}文件名称:{operation.file_name}"
        elif operation.project_name and not operation.file_name:
            formatted_content = f"{operation.content}项目名称:{operation.project_name}"
        else:
            formatted_content = f"{operation.content}"
        operations_list.append({
            "id": operation.id,
            "user": operation.user,
            "code": 0,
            "timestamp": operation.timestamp,
            "formatted_content": formatted_content
        })
    data = len(operations_list)
    return JsonResponse({"code":0, "msg": "模糊搜索成功", "operations": operations_list, "pagination": data })
