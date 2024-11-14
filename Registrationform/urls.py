from django.contrib import admin
from django.urls import path
from app1 import views 

urlpatterns = [
    path('admin/', admin.site.urls),  
    path('', views.login_attempt, name='login_attempt'), 
    path('success/', views.success_page, name='success_page'),
]
