from django.shortcuts import render
from django.shortcuts import get_object_or_404

# importing apiview and response to write api's and controller's logic
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# importing models
from .models import Staff
from .models import StudentsDatabase
from .models import Department

# importing serializer
from .serializer import StaffSerializer
from .serializer import StudentSerializer

# Create your views here.
@api_view(["GET"])
def get_staff(request):
    try:
        staffs = Staff.objects.all()
        serializer_response = StaffSerializer(staffs, many=True)

        return Response(serializer_response.data)
    except:
        return print("Internal server error")
     
# get one staff with id
@api_view(["GET"])
def get_one_staff(request, staff_id):
    try:
        one_staff = get_object_or_404(Staff, id=staff_id)
        serializer_response = StaffSerializer(one_staff)

        return Response(serializer_response.data)
    except:
        return print("Internal server error")


@api_view(["DELETE"])
def delete_staff(request, staff_id):
    try:
        staff_member = get_object_or_404(Staff, id=staff_id)
        staff_member.delete()
        return Response(
            {"message": "Staff deleted successfully"},
           
        )
    except Exception as e:
        return Response(
            {"error": str(e)},
        )


# Update staff with id
@api_view(["PUT"])
def update_staff(request, staff_id):
    try:
        staff_member = get_object_or_404(StudentsDatabase, id=staff_id)
        serializer = StudentSerializer(staff_member, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors)
    except Exception as e:
        return Response(
            {"error": str(e)}, 
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )