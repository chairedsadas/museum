from django.urls import path
from . import views

app_name = 'educationAPP'
urlpatterns = [
    path('culture/', views.culture, name='culture'),  # 文化
    path('history/', views.history, name='history'),  # 历史
]
