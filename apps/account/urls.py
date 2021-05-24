from django.urls import path

from . import views
app_name = 'account'
urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_request, name='login'),
    path('student_register/', views.StudentRegister, name='student_register'),
    path('coordinator_register/', views.CoordinatorRegister, name='coordinator_register'),
    path('logout/', views.logout, name='logout')
]
