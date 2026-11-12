from django.urls import path
from . import views

urlpatterns = [
    path("staff/", views.get_staff), 
    path("staff/<int:staff_id>/", views.get_one_staff),
    path("staff/delete/<int:staff_id>", views.delete_staff),
    path("staff/update/<int:staff_id>/", views.update_staff),
] 