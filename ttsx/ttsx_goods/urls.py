from django.conf.urls import url
from ttsx_goods import views


urlpatterns = [
    url(r'^$',views.index),
    url(r'^index/$',views.index),

]