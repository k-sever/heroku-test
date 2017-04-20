from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    # url(r'^post$', csrf_exempt(views.index), name='index'),
    url(r'^post$', csrf_exempt(views.test), name='test'),
]