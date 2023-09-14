# 功能说明
![img.png](img.png)
# 代码说明
· 前端 vue

· 后端 python3

· 数据库 mysql8

· 存储 NFS
# 目录说明
![img_1.png](img_1.png)![img_2.png](img_2.png)

pms： 项目主目录

api： 接口入口目录

customerProjects: 定制化项目接口

fileManager: 文件相关接口

mainProjects: 主线项目接口

operationHistory：操作日志接口

products：产品接口

users： 用户接口

# 安装
- 数据库安装
```shell
# ll
-rw-r--r-- 1 root    root  222 Jul  3 09:56 docker-compose.yaml
drwxr-xr-x 8 polkitd root 4096 Jul  3 10:29 mysql_data
#
cat docker-compose.yaml
version: '3'
services:
  mysql:
    image: mysql:8
    restart: always
    environment:
      MYSQL_ROOT_PASSWORD: admin1234
    ports:
      - 3307:3306 #宿主机:容器
    volumes:
      - ./mysql_data:/var/lib/mysql
```
- nfs安装(略)
```shell
# cat /etc/exports
/data/nfs/pms *(rw,sync,no_root_squash)
```
- 代码拉取
```shell
# git init
# git remote add origin https://github.com/yinfuqian/pms.git
# git pull origin mastger
```
- 修改后端配置
```shell
vim  pms/settings.py
```
![img_3.png](img_3.png)
![img_4.png](img_4.png)

