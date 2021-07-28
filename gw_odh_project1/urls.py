"""gw_odh_project1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from gw_odh_project1 import settings

urlpatterns = [
    path('admin/', admin.site.urls), #관리자 페이지에 관한 설정
    path('accounts/', include('accountapp.urls')),
    path('profiles/', include('profileapp.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)#어디로 ~하면 어디로 돌려 줄것인지, django의 cong에 있는 static가져와야한다.

