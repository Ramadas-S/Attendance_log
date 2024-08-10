from django.shortcuts import redirect, render
from . models import StaffMaster,AttendanceLog
from .forms import StaffMasterForm , AttendanceLogForm
from django.contrib import messages

# Create your views here.

def landing_page(request):
    
    return render(request, 'landing_page.html')

def add_member(request):
    if request.method == 'POST':
        form = StaffMasterForm(request.POST)
        
        if StaffMaster.objects.filter(name__iexact=form.data['name']).exists():
            messages.error(request, 'This staff member already exists.')
        elif form.is_valid():
            form.save()
            messages.success(request, 'Staff member added successfully!')
            return redirect('mark_attendance')  # redirect after POST
        else:
            messages.error(request, 'There was an error adding the staff member. Please try again.')
    else:
        form = StaffMasterForm()

    return render(request, 'staff_names.html', {'form': form})


def mark_attendance(request):
    if request.method == 'POST':
        form = AttendanceLogForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Attendance logged successfully!')
            return redirect('attendance_report')
    else:
        form = AttendanceLogForm()

    return render(request, 'attendance.html', {'form': form})


def attendance_report(request):
   
    attendance_logs = AttendanceLog.objects.select_related('staff').all()   # Fetch all attendance logs and related staff members
   
    return render(request, 'attendancelogreport.html', {'attendance_logs': attendance_logs})