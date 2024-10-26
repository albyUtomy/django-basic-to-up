from django.urls import path
from .views import DepartmentCrud,Department_by_Id


urlpatterns = [
    path('', DepartmentCrud.as_view(), name="department-crud"),
    path('department/<int:department_id>/',Department_by_Id.as_view(), name='details-by-id'),

    ]