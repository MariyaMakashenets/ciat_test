from django.conf.urls import url
from .views import *

urlpatterns = [
    url('', all_currencies, name='currencies'),

]
