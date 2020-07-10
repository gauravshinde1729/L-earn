from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.tutorLogin,name="tutorLogin"),
    path('home/', views.tutorHome,name="tutorHome"),

]
