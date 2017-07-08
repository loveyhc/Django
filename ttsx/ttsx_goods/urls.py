from django.conf.urls import url, include, patterns
from ttsx_goods import views


urlpatterns = [
    url(r'^$',views.index),
    url(r'^index/$',views.index),
    url(r'^list(\d{0,1})(\d*)',views.goods_list),
    url(r'^tag/$',views.tag),

]