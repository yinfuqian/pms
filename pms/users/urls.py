from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.login),
    path('check_token/', views.check_token),
    path('get/', views.get_user),
    path('search/', views.search_user),
    path('create', views.create_user),
    path('update/<int:user_id>', views.update_user),
    path('delete/<int:user_id>', views.delete_user),
]