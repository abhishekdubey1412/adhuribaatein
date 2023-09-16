"""
URL configuration for adhuribaatein project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from services import views as services_views
from user import views as user_views

urlpatterns = [
    path('admin-panel/', admin.site.urls),
    path('', services_views.home, name='home'),
    path('about-us/', services_views.about, name='about'),
    path('registration/', user_views.registration, name='registration'),
    path('login/', user_views.loginsuer, name='loginsuer'),
    path('love/', services_views.love, name='love'),
    path('sad/', services_views.sad, name='sad'),
    path('romantic/', services_views.romantic, name='romantic'),
    path('story/', services_views.story, name='story'),
    path('camera/', services_views.camera, name='camera'),
    # path('get_ip/', services_views.get_user_ip, name='get_user_ip'),
]