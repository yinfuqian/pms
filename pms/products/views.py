# Create your views here.
from django.db.models import Q
from django.http import JsonResponse
from rest_framework.decorators import api_view

from .models import PmsProductsList


@api_view(['GET'])
# 所有列表
def products_list(request):
    products = PmsProductsList.objects.all()
    page_num = request.GET.get('pageNum')
    page_size = request.GET.get('pageSize')
    start = (int(page_num) - 1) * int(page_size)
    end = start + int(page_size)
    page_products = products[start:end]
    count = products.count()
    products_list = []
    for product in page_products:
        products_list.append({
            "id": product.id,
            "code": 0,
            "product_name": product.product_name,
            "product_version": product.product_version,
            "product_install_method": product.product_install_method,
            "product_notes": product.product_notes})
    data = {
        'count': count,
    }
    return JsonResponse({"code": 0, "msg": "获取所有产品成功", "products": products_list, "pagination": data})


# 搜索产品
def search_product(request):
    product_name = request.GET.get('product_name')
    product_id = request.GET.get('id')
    try:
        product_list = []
        if product_id:
            # 根据id搜索产品
            product = PmsProductsList.objects.get(id=product_id)
            product_list.append({
                "id": product.id,
                "code": 0,
                "product_name": product.product_name,
                "product_version": product.product_version,
                "product_install_method": product.product_install_method,
                "product_notes": product.product_notes
            })
        elif product_name:
        # 区分大小写
            products = PmsProductsList.objects.filter(
                Q(product_name__exact=product_name) | Q(product_name__iexact=product_name))
            for product in products:
                product_list.append({
                    "id": product.id,
                    "code": 0,
                    "product_name": product.product_name,
                    "product_version": product.product_version,
                    "product_install_method": product.product_install_method,
                    "product_notes": product.product_notes
                })
        return JsonResponse({"code": 0, "msg": "查询产品成功", "products": product_list})
    except Exception as e:
        return JsonResponse({
            'message': '产品不存在',
            'code': '1'
        }, status=404)

# 创建产品
@api_view(['POST'])
def create_product(request):
    reversed = request.POST
    product_name = reversed.get('product_name')
    product_version = reversed.get('product_version')
    product_install_method = reversed.get('product_install_method')
    product_notes = reversed.get('product_notes')
    # undefine 转为none
    if product_install_method == 'undefined':
        product_install_method = None
    if product_notes == 'undefined':
        product_notes = None
        # 如果传值为空，则使用默认值
    if not product_install_method:
        product_install_method = PmsProductsList._meta.get_field('product_install_method').get_default()
    if not product_notes:
        product_notes = PmsProductsList._meta.get_field('product_notes').get_default()
    try:
        # 检查产品是否已经存在
        if PmsProductsList.objects.filter(product_name=product_name, product_version=product_version).exists():
            return JsonResponse({"code": 2, "msg": "该版本产品已存在，请勿重复创建"})
        # 创建产品
        product = PmsProductsList.objects.create(product_name=product_name, product_version=product_version,
                                                 product_install_method=product_install_method,
                                                 product_notes=product_notes)
        return JsonResponse({"code": 0, "msg": "产品创建成功"})
    except Exception as e:
        print(e)
        return JsonResponse({"code": 1, "msg": "产品创建失败"})


# 删除产品
@api_view(['DELETE'])
def delete_product(request, product_id):
    try:
        product = PmsProductsList.objects.get(id=product_id)
    except PmsProductsList.DoesNotExit:
        return JsonResponse({"code": 2, "msg": "产品不存在"})
    try:
        product.delete()
        return JsonResponse({"code": 0, "msg": "产品删除成功"})
    except Exception as e:
        print(e)
        return JsonResponse({"code": 1, "msg": "产品删除失败"})


@api_view(['PUT'])
# 更新产品
def update_product(request, product_id):
    try:
        product = PmsProductsList.objects.get(id=product_id)
    except PmsProductsList.DoesNotExist:
        return JsonResponse({"code": 1, "msg": "产品不存在"})

    reversed = request.data
    product_name = reversed.get('product_name')
    product_version = reversed.get('product_version')
    product_install_method = reversed.get('product_install_method')

    product_notes = reversed.get('product_notes')
    if reversed.get('product_name'):
        product.product_name = product_name
    if reversed.get('product_version'):
        product.product_version = product_version
    if reversed.get('product_install_method'):
        product.product_install_method = product_install_method
    if reversed.get('product_notes'):
        product.product_notes = product_notes
    try:
        product.save()
        return JsonResponse({"code": 0, "msg": "产品更新成功"})
    except Exception as e:
        print(e)
        return JsonResponse({"code": 1, "msg": "产品更新失败"})


