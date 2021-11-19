"""example URL Configuration

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
from django.contrib import admin
from django.urls import path, include
from app import views
# app 파일 안에 있는 views를 가져옴

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
    path('lotto/', views.lotto),
    path('computer/', views.computer),
    path('hi/<str:name>/', views.hi),
    path('add/<int:a>/<int:b>/', views.add),
    path('posts/<int:id>/', views.posts),
    
    path('articles/', include('articles.urls')),
]

# view로 들어갈 수 있는 path 설정인 것이다.
# 즉, 이정표의 역할을 하며 대응되는 함수를 실행시킨다. 
# index가 들어오면 views 안에 있는 index 함수를 실행하겠다는 의미