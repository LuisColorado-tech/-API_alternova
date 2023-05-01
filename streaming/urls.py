"""
URL configuration for streaming project.

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
from streamingapi import views
from django.contrib.auth.views import LoginView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('obtener_aleatoria/<str:tipo>/', views.obtener_aleatoria, name='obtener_aleatoria'),
    path('obtener_todas/<str:tipo>/<str:orden>/', views.obtener_todas, name='obtener_todas'),
    path('filtrar/<str:tipo>/', views.filtrar, name='filtrar'),
    path('marcar_vista/<str:tipo>/<int:id>/', views.marcar_vista, name='marcar_vista'),
    path('puntuar/<str:tipo>/<int:id>/<int:puntuacion>/', views.puntuar, name='puntuar')
]
