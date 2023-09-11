import os

import paramiko
from django.conf import settings
from django.http import FileResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# 配置SSH连接信息
nfs_server_host = settings.NFS_SERVER_IP
nfs_server_port = settings.NFS_SERVER_PORT
nfs_server_username = settings.NFS_SERVER_USERNAME
nfs_server_password = settings.NFS_SERVER_PASSWORD
nfs_shared_path = settings.NFS_SERVER_PATH


# 上传
@csrf_exempt
def upload_file(request):
    if request.method == 'POST' and request.FILES.get('file') and 'project_name' in request.POST:
        try:
            # 获取上传的文件
            uploaded_file = request.FILES['file']
            project_name = request.POST.get('project_name')
            # print(project_name)
            # 获取参数（'main' 或 'customers'）
            directory_type = request.POST.get('directory_type')
            # print(directory_type)
            if directory_type == 'main':
                base_directory = 'main'
            elif directory_type == 'customers':
                base_directory = 'customers'
            else:
                return JsonResponse({'error': '无效的目录类型'}, status=400)

            # 创建SSH客户端连接
            ssh_client = paramiko.SSHClient()
            ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh_client.connect(nfs_server_host, port=nfs_server_port,
                               username=nfs_server_username, password=nfs_server_password)

            # 创建目录（如果不存在）
            parent_dir = os.path.join(nfs_shared_path, base_directory)
            target_dir = os.path.join(nfs_shared_path, base_directory, project_name)
            # print(target_dir)
            target_dir = target_dir.replace('\\', '/')
            # print(target_dir)
            # 使用SSH连接进行SFTP操作
            sftp = ssh_client.open_sftp()
            # 创建父级目录
            try:
                sftp.stat(parent_dir)
            except FileNotFoundError:
                sftp.mkdir(parent_dir)
            # 检查目录是否存在，如果不存在则创建
            try:
                sftp.stat(target_dir)
            except FileNotFoundError:
                sftp.mkdir(target_dir)
            # 保存文件到本地临时目录
            temp_file_path = f'../tmp/{uploaded_file.name}'
            with open(temp_file_path, 'wb') as temp_file:
                for chunk in uploaded_file.chunks():
                    temp_file.write(chunk)

            # 使用SSH连接将文件上传到NFS服务器
            nfs_file_path = os.path.join(target_dir, uploaded_file.name)
            # print(nfs_file_path)
            # 将路径分隔符替换为正斜杠，以便系统正确解析路径
            nfs_file_path = nfs_file_path.replace('\\', '/')
            sftp.put(temp_file_path, nfs_file_path)

            # 删除本地临时文件
            os.remove(temp_file_path)

            ssh_client.close()

            return JsonResponse({'message': f'文件 {uploaded_file.name} 上传到nfs'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': '方法不被允许'}, status=400)


# 展示
@csrf_exempt
def list_file(request):
    project_type = request.GET.get('project_type')
    project_name = request.GET.get('project_name')
    # 创建SSH客户端连接
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh_client.connect(nfs_server_host, port=nfs_server_port,
                           username=nfs_server_username, password=nfs_server_password)

        # 构建NFS目录路径
        nfs_directory = os.path.join(nfs_shared_path, project_type, project_name)
        target_dir = nfs_directory.replace('\\', '/')
        # print(target_dir)

        # 使用SSH连接进行SFTP操作
        sftp = ssh_client.open_sftp()

        try:
            file_list = sftp.listdir(target_dir)
        except FileNotFoundError:
            return JsonResponse({'error': '指定的目录不存在'}, status=404)
    finally:
        sftp.close()
        ssh_client.close()

    return JsonResponse({'files': file_list})


# 下载

def download_file(request):
    project_type = request.GET.get('project_type')
    project_name = request.GET.get('project_name')
    file_name = request.GET.get('file_name')
    #print(file_name)
    # 构建文件的完整路径
    file_path = os.path.join(nfs_shared_path, project_type, project_name, file_name)
    target_dir = file_path.replace('\\', '/')
    # 检查文件是否存在
    # 创建SSH客户端连接
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(nfs_server_host, port=nfs_server_port, username=nfs_server_username,
                           password=nfs_server_password)
    sftp = ssh_client.open_sftp()
    try:
            sftp.stat(target_dir)
    except FileNotFoundError:
            return JsonResponse({'error': '文件不存在'}, status=404)
    # 打开文件并创建 FileResponse
    file_handle = sftp.file(target_dir, 'rb')
    response = FileResponse(file_handle)

    # 设置Content-Disposition头，指定下载的文件名
    response['Content-Disposition'] = f'attachment; filename="{file_name}"'
    return response
