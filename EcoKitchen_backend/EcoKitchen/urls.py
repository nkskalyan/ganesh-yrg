from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^signin', views.signInUser),
    url(r'^signin_mock', views.signInUser),
]
