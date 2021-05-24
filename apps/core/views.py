from django.shortcuts import render

def frontpage(request):
    return render(request, 'core/index.html')

def StudentDashboard(request):
    return render(request, 'core/studentView/student_dashboard.html')

def coordinatorDashboard(request):
    return render(request, 'core/coordinatorView/coordinator_dashboard.html')