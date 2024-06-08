from django.urls import path
from . import views

app_name = 'collectionAPP'

urlpatterns = [
    path('penmanship/', views.penmanship, name='penmanship'),  # 书法
    path('Bronze_ware/', views.Bronze_ware, name='Bronze_ware'),  # 青铜器
    path('porcelain/', views.porcelain, name='porcelain'),  # 瓷器
]
