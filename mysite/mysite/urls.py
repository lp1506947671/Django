"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, re_path, include

from my_url_controller import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index),
    # re_path:简单的路由配置
    re_path("^my_url_controller/([0-9]{4})/([0-9]{2})/$", views.my_url_controller_demo1),
    # re_path:有名分组
    re_path("^my_url_controller/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]+)/$",
            views.my_url_controller_demo2),
    # include:分发 namespace:命名空间
    path("my_url_controller/", include("my_url_controller.urls", namespace="my_url_controller")),
    path("my_url_controller1/", include("my_url_controller.urls", namespace="my_url_controller1")),

    path("my_url_controller2/", include("my_url_controller2.urls", namespace="my_url_controller2")),
    path("my_model/", include("my_model.urls")),
    path("book_app/", include("book_app.urls")),
    path("books_app/", include("books_app.urls"))
]
