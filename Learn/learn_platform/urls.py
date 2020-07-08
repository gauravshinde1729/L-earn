from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name="platform_home"),
    path('logout/',views.logoutPage,name="Logoutpage"),
    path('profilepage/',views.profilePage,name="profilePage")
]
