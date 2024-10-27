from django.urls import path
from .views import DepartmentCrud,Department_by_Id, DepartmentSort


urlpatterns = [
    path('', DepartmentCrud.as_view(), name="department-crud"),
    path('department/<int:department_id>/',Department_by_Id.as_view(), name='details-by-id'),
    path('department_filter/<int:department_id>/', DepartmentSort.as_view(), name='filter'),
    path('department_teacher/<str:department_id>/', DepartmentSort.as_view(), name='filter'),
    path('department_student/<int:department_id>/', DepartmentSort.as_view(), name='filter'),
    # path('department_filter/<int:department_id>/', DepartmentSort.as_view(), name='filter'),
    ]