from django.db import models

# Create your models here.

class StaffMaster(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    
    class Meta:
        db_table = 'staff_master'  # This tells Django to use the existing table
        managed = False  # This prevents Django from managing migrations
    
    def __str__(self):
        return self.name


class AttendanceLog(models.Model):
    id = models.AutoField(primary_key=True)
    staff = models.ForeignKey(StaffMaster, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(max_length=10)

    class Meta:
        db_table = 'attendance_log'  # This tells Django to use the existing table
        managed = False  # This prevents Django from managing migrations
        
    def __str__(self):
        return f"{self.staff.name} - {self.date} - {self.status}"
    