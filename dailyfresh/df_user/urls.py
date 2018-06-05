from django.conf.urls import url

from.views import *


urlpatterns = [
      url(r'^register/$',register, name='register'),
    url(r'^register_handle/$',register_handle, name='register_handle'),

]