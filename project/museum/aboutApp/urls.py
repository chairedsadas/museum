from django.urls import path
from . import views

app_name = 'aboutAPP'

urlpatterns = [
    path('introduce/', views.introduce, name='introduce'),  # 总体介绍
    path('leader/', views.leader, name='leader')  # 领导

]
