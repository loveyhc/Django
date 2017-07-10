from django.conf.urls import url, include, patterns
from ttsx_goods import views


urlpatterns = [
    url(r'^$',views.index),
    url(r'^index/$',views.index),
    url(r'^list(\d?)(\d*)',views.goods_list),
    # url(r'^list_tag/$',views.list_tag),
    url(r'^detail(\d?)(\d*)',views.detail),

]