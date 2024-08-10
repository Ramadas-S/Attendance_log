from django.urls import path
from . import views

urlpatterns = [
    path('add_member/',views.add_member,name='add_member'),
    # path('success_page/', views.success_page, name='success_page'),
]
