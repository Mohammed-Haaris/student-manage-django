from django.urls import path
from . import views

urlpatterns = [
    path("staff/", views.get_staff),
    path("all/staff/", views.get_staffs),
    path("staff/<int:staff_id>/", views.get_one_staff)
]