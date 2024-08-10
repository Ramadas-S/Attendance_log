from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'), 
    path('add_member/',views.add_member,name='add_member'),
    path('mark/', views.mark_attendance, name='mark_attendance'),
    path('report/', views.attendance_report, name='attendance_report'),
]
