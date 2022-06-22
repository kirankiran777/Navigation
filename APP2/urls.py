from django.urls import path
from APP2.views import *
app_name='APP2'

urlpatterns=[
    path('bye/',bye,name='bye'),
]