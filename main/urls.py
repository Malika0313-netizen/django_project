from .views import *
from django.urls import path

urlpatterns = [
    path('', home, name='home'),
    path('batken/', batken, name='batken'),
    path('osh/', osh, name='osh'),
    path('jalal_abad/', jalal_abad, name='jalal_abad'),
    path('naryn/', naryn, name='naryn'),
    path('issyk_kul/', issyk_kul, name='issyk_kul'),
    path('talas/', talas, name='talas'),
    path('chuy/', chuy, name='chuy'),

#     район
    path('batken/raiony/', r_batken, name='r_batken'),
    path('chuy/raiony/', ch_raion, name='ch_raion'),
    path('issyk_kul/raiony/', issyk_raion, name='issyk_kul'),
    path('jalal_abad/raiony/', jalal_raion, name='jalal_abad'),
]