"""myfirst_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls,),
    path('', views.home_page_view, name='home'),
    path('about/', views.about_page_view, name='about'),
    # path('signin/', views.Sign_in, name ='signin'),
    # path('logout/', views.sign_out, name = 'logout'),
    # path('signup/', views.SignUP, name = 'signup'),
    path('detail/<int:pk>/', views.FireRecordDetail.as_view(), name='detail'),
    path('results/', views.FireRecordListView.as_view(), name='list'),
    path('delete/<int:pk>/', views.FireRecordDelete.as_view(), name='delete'),
    path('rpi_request/', views.recieve_data_from_rpi, name="rpi_request"),

]
