"""login URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from loginapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', views.index),
    #path('index/', views.index),
 
    #path('login/', views.login),
    #path('logout/', views.logout),    
     
    path('adduser/', views.adduser), 
]

#ref:
#http://ivanjo39191.pixnet.net/blog/post/150982914-python-django-%E5%AD%B8%E7%BF%92%E7%B4%80%E9%8C%84%28%E4%B8%83%29-%E4%BD%BF%E7%94%A8%E8%80%85%E7%AE%A1%E7%90%86