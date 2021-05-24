from django import urls
from django.urls import path

from . import views

app_name = 'core'
urlpatterns = [
    path('', views.frontpage, name="frontpage"),
    path('student/Dashboard/', views.StudentDashboard, name="student-dashboard"),
    path('coordinator/Dashboard/', views.coordinatorDashboard, name="coordinator-dashboard"),
]
