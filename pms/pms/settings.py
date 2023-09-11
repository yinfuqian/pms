from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-e*8+foal90khwo+_u%y&p2$!al7@8@v=9&+#r2$iczh9!cp)4_'

DEBUG = True
# 允许主机
ALLOWED_HOSTS = ["*"]
# 　导入应用
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'pms',
    'api',
    'users',
    'products',
    'customerProjects',
    'mainProjects',
    'corsheaders',
    'fileManager',
]

# rest 配置
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'users.auth.ExpiringTokenAuthentication',
    ),

    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ),
}

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',   # 禁用csrf 保护
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]

# 跨域处理
CORS_ORIGIN_ALLOW_ALL = True
# 允许携带身份凭证（例如 Cookie）
# CORS_ALLOW_CREDENTIALS = True
# 允许的前端地址
CORS_ALLOW_ORIGINS = [
    '*',
]

CORS_ORIGIN_WHITLIST = ["*"]
# 允许的请求方法
CORS_ALLOW_METHODS = [
    'GET',
    'POST',
    'PUT',
    'PATCH',
    'DELETE',
]

# 允许的请求头
CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
]


# 缓存
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}

ROOT_URLCONF = 'pms.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'pms.wsgi.application'

# 指定自定义模型
AUTH_USER_MODEL = 'users.PmsUserProfile'

# 数据库配置
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'pms',
        'USER': 'root',
        'PASSWORD': 'admin1234',
        'HOST': '172.16.20.153',
        'PORT': '3307'
    }
}

# 降低密码强度
AUTH_PASSWORD_VALIDATORS = []

# 语言
LANGUAGE_CODE = 'zh-hans'
TIME_ZONE = 'Asia/Shanghai'
USE_I18N = True
USE_TZ = False
# 静态资源
STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# nfs配置
NFS_SERVER_IP = '172.16.20.153'
NFS_SERVER_PORT = '22'
NFS_SERVER_USERNAME = 'root'
NFS_SERVER_PASSWORD = '1'
NFS_SERVER_PATH = '/data/nfs/pms/'

