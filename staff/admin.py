from django.contrib import admin
from .models import StaffMaster, AttendanceLog

# Register your models here.

@admin.register(StaffMaster)
class StaffMasterAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')  # to display name & Id in admin page
    search_fields = ('name',)  # field to search by names
    ordering = ('id',) #  order by id

@admin.register(AttendanceLog)
class AttendanceLogAdmin(admin.ModelAdmin):
    list_display = ('id', 'staff', 'date', 'time', 'status')  
    list_filter = ('date', 'status')  # for filtering
    search_fields = ('staff__name',)  