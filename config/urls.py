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
from django.urls import path

import project.api.views as views


urlpatterns = [
    path("admin/", admin.site.urls, name="admin"),
    path("admin/", admin.site.urls, name="admin"),
    path("api/factories/", views.factories, name="factories"),
    path("api/factory/<int:factory_id>/", views.factory, name="factory"),
    path("api/factory/<int:factory_id>/chart-data/", views.chart_data, name="chart_data"),
    path("api/factory/<int:factory_id>/production-actual/", views.production_actual, name="production"),
    path("api/factory/<int:factory_id>/production-goal/", views.production_goal, name="production_goal"),
    path("api/factory/<int:factory_id>/time/", views.time, name="time"),
    path("api/sprockets/", views.sprockets, name="sprockets"),
    path("api/sprocket/<int:sprocket_id>/", views.sprocket, name="sprocket"),
    path("api/sprocket/<int:sprocket_id>/update/<int:teeth>/<int:pitch_diameter>/<int:outside_diameter>/<int:pitch>/", views.sprocket_update, name="sprocket_update"),
    path("api/sprocket/create/<int:teeth>/<int:pitch_diameter>/<int:outside_diameter>/<int:pitch>/", views.sprocket_create, name="sprocket_create"),
]
