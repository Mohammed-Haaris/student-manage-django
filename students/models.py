from django.db import models

# Create your models here.
class Staff(models.Model):
    staff_name = models.CharField(max_length=80)
    staff_joined = models.IntegerField()

    def __str__(self):
        return self.staff_name

class Department(models.Model):
    dept_name = models.CharField(max_length=100)
    dept_staff = models.ForeignKey(Staff, on_delete=models.CASCADE)

    def __str__(self):
        return self.dept_name


class StudentsDatabase(models.Model):
    stud_name = models.CharField(max_length=80)
    stud_city = models.CharField(max_length=100)
    stud_dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    stud_staff = models.ForeignKey(Staff, on_delete=models.CASCADE)

    def __str__(self):
        return self.stud_name 