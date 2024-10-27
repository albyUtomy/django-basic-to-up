from django.urls import path
from .views import SchoolCrud, SchoolUpdateRetrieveView, Filtration


urlpatterns = [
    path('', SchoolCrud.as_view(), name="school-crud"),
    path('school_details/<int:school_id>/',SchoolUpdateRetrieveView.as_view(), name='school-update-retrieve'),
    path('school/departments/<int:school_id>', Filtration.as_view(), name='school_departments'),
    path('school/teachers/<int:school_id>', Filtration.as_view(), name='teacher_name'),
    path('school/students/<int:school_id>', Filtration.as_view(), name='school_students')
    ]