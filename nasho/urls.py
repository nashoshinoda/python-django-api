from nasho import views
from django.urls import path, include
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'programmers', views.ProgrammerViewSet)  #programmers endpoint

urlpatterns = [
    path('', include(router.urls))
]

