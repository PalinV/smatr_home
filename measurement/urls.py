from django.urls import path

from measurement.views import SensorAPIView, SensorUpdateAPIView, OneSensorAPIView

urlpatterns = [
    path('sensors/', SensorAPIView.as_view()),
    path('measurements/', SensorUpdateAPIView.as_view()),
    path('sensors/<pk>/', OneSensorAPIView.as_view()),

]
