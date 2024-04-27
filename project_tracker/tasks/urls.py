from django.urls import path
from tasks import views
# from quality_control import views

app_name = 'tasks'

urlpatterns = [
    path('', views.index),
    path('another/', views.another_page, name='another_page'),
    # path('quality_control/', quality_control.views.index),
]
