from django.shortcuts import render
from . models import StaffMaster
from .forms import StaffMasterForm

# Create your views here.

def add_member(request):
    
    form = StaffMasterForm()
    
    return render(request,'staff_names.html',{'form': form})