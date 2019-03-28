"""compton URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from apps.races import views


urlpatterns = [
    url(r'^$', views.loginReg),
    url(r'^dashboard$', views.dashboard),
    url(r'^assignments$', views.assignments),
    url(r'^add$', views.add),
    url(r'^registration$', views.registration),
    url(r'^login$', views.login),
    url(r'^addrace$', views.addrace),
    url(r'^edit/(?P<race_id>\d+)$', views.edit),
    url(r'^canwork/(?P<race_id>\d+)$', views.canwork),
    url(r'^cantwork/(?P<race_id>\d+)$', views.cantwork),
    url(r'^signout$', views.signout),
    url(r'^delete/(?P<race_id>\d+)$', views.delete)
]

#url(r'^dashboard/(?P<user_id>\d+)$', views.dashboard),