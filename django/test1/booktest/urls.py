from django.conf.urls import url
from booktest import views

urlpatterns=[
    url(r'^$',views.index),
    url(r'^delete(\d+)/$',views.delete),
    url(r'^create/$',views.create),
    # 配置详细页url，\d+表示多个数字，小括号用于取值，建议复习下正则表达式
    url(r'^(\d+)/$', views.detail),
    url(r'^cookie_set/$', views.cookie_set),

]