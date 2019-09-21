from django.conf.urls import url
from . import views
urlpatterns = [
    # 当用户访问bookApp应用的主页时, 执行视图函数index,反向根据名称获取url地址;
    url(r'^$', views.index, name='index'),
    url(r'^([0-9]+)/$', views.detail, name='detail'),
]