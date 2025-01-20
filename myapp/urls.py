from django.urls import path,include
from .views import *

urlpatterns = [
    path('',data,name='data'),
    path('login/',login,name='login'),
    path('logout/',logout,name='logout'),
    path('reg/',reg,name="reg"),
]
