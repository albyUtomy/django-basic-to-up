
from django.urls import path, include
from .views import StudentCrudOperation,SortByTeacher,StudentMarkFiltration, StudentModification, StudentSortedBy

urlpatterns = [
    path('', StudentCrudOperation.as_view(), name="list_students"),
    path('student/<int:roll_no>', StudentModification.as_view(), name="student"),
    path('subject/<str:subject>/', StudentSortedBy.as_view(), name="chemistry-marks"),
    path('class_teacher/<str:teacher_name>/', SortByTeacher.as_view(), name="class_teacher"),
    path('statics/<str:filtration>/', StudentMarkFiltration.as_view(), name="average_marks"),
]