from django.conf.urls import url
from .api import *
urlpatterns = [
    url('api/outcode/(?P<outcode>[\w\s]+)$',postalcodeapi),
    url('api/nexus/(?P<outcode>[\w\s]+)$',nexuspoutcodeapi)
]
