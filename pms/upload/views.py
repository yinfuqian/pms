import os
import paramiko
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import logging
logger = logging.getLogger(__name__)
@csrf_exempt
def upload_file(request):
    if request.method == 'POST' and request.FILES.get('file') and 'project_name' in request.POST:
        try:
            # 获取上传的文件
            uploaded_file = request.FILES['file']
            project_name = request.GET.get('project_name')
            project_name = str(project_name)
            # 配置SSH连接信息
            nfs_server_host = settings.NFS_SERVER_IP
            nfs_server_port = settings.NFS_SERVER_PORT
            nfs_server_username = settings.NFS_SERVER_USERNAME
            nfs_server_password = settings.NFS_SERVER_PASSWORD
            nfs_shared_path = settings.NFS_SERVER_PATH
            # 创建SSH客户端连接
            ssh_client = paramiko.SSHClient()
            ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh_client.connect(nfs_server_host, port=nfs_server_port,
                               username=nfs_server_username, password=nfs_server_password)

            # 创建目录（如果不存在）
            target_dir = os.path.join(nfs_shared_path, project_name)
            # 使用SSH连接进行SFTP操作
            sftp = ssh_client.open_sftp()

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
            # 将路径分隔符替换为正斜杠，以便系统正确解析路径
            nfs_file_path = nfs_file_path.replace('\\', '/')
            sftp.put(temp_file_path, nfs_file_path)
            print(nfs_file_path)
            # 删除本地临时文件
            os.remove(temp_file_path)

            ssh_client.close()

            return JsonResponse({'message': f'File {uploaded_file.name} uploaded to NFS.'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'File not provided or method not allowed.'}, status=400)
