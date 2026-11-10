from django.shortcuts import render
from django.shortcuts import get_object_or_404

# importing apiview and response to write api's and controller's logic
from rest_framework.decorators import api_view
from rest_framework.response import Response

# importing models
from .models import Staff
from .models import StudentsDatabase
from .models import Department

# importing serializer
from .serializer import StaffSerializer
from .serializers import StaffSerializers

# Create your views here.
@api_view(["GET"])
def get_staff(request):
    try:
        staffs = Staff.objects.all()
        serializer_response = StaffSerializer(staffs, many=True)

        return Response(serializer_response.data)
    except:
        return print("Internal server error")


@api_view(["GET"])
def get_one_staff(request, staff_id):
    try:
        one_staff = get_object_or_404(Staff, id=staff_id)
        serializer_response = StaffSerializer(one_staff)

        return Response(serializer_response.data)
    except:
        return print("Internal server error")

# get staff all
@api_view(["GET"])
def get_staffs(request):
    try:
        fetch_staff = Staff.objects.all()

        serialize_response = StaffSerializers(fetch_staff, many=True)

        return Response(serialize_response.data)
    except:
        return print("Internal Server Error")