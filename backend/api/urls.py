"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from .views.pacient_views import pacientlist
from .views.doctor_views import doctorlist
from .views.queue_views import queuelist
from .views.reception_views import receptionlist
from .views.service_views import servicelist



urlpatterns = [
    path('pacients/', pacientlist, name="list-pacients"),
    path('doctors/', doctorlist, name="list-doctors"),
    path('queues/', queuelist, name="list-queues"),
    path('receptions/', receptionlist, name="list-receptions"),
    path('services/', servicelist, name="listservice"),
]
