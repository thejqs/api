"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import re_path

import project.api.views as views


urlpatterns = [
    re_path(r"admin/", admin.site.urls, name="admin"),
    re_path(r"^api/factories/$", views.factories, name="factories"),
    re_path(r"^api/factory/(\d)/$", views.factory, name="factory"),
    re_path(r"^api/factory/(\d)/chart-data/$", views.chart_data, name="chart_data"),
    re_path(r"^api/factory/(\d)/production-actual/$", views.production_actual, name="production"),
    re_path(r"^api/factory/(\d)/production-goal/$", views.production_goal, name="production_goal"),
    re_path(r"^api/factory/(\d)/time/$", views.time, name="time"),
    re_path(r"^api/sprockets/$", views.sprockets, name="sprockets"),
    re_path(r"^api/sprocket/(\d)/$", views.sprocket, name="sprocket"),
    re_path(r"^api/sprocket/create/(?P<teeth>\d)/(?P<pitch_diameter>\d)/(?P<outside_diameter>\d)/(?P<pitch>\d)/$", views.sprocket_create, name="sprockets_create"),
    re_path(r"^api/sprocket/(\d)/update/$", views.sprocket_update, name="sprocket_update"),

]
