from rest_framework import serializers
from .models import StudentsDatabase
from .models import Staff
from .models import Department


class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = "__all__"


class DepartmentSerializer(serializers.ModelSerializer):

    dept_staff = StaffSerializer(read_only=True)
    
    class Meta:
        model = Department
        fields = "__all__"

class StudentSerializer(serializers.ModelSerializer):

    # For GET: Display complete Staff details
    staff_details = StaffSerializer(
        source="stud_staff",
        read_only=True
    )

    # For GET: Display complete Department details
    department_details = DepartmentSerializer(
        source="stud_dept",
        read_only=True
    )

    # For POST/PUT/PATCH: Accept Staff ID
    stud_staff = serializers.PrimaryKeyRelatedField(
        queryset=Staff.objects.all()
    )

    # For POST/PUT/PATCH: Accept Department ID
    stud_dept = serializers.PrimaryKeyRelatedField(
        queryset=Department.objects.all()
    )

    class Meta:
        model = StudentsDatabase
        fields = "__all__"