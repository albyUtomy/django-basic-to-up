
from django.urls import path, include
from .views import StudentCrudOperation,SortByTeacher,StudentMarkStatistic, StudentModification, StudentSortedBy

urlpatterns = [
    path('', StudentCrudOperation.as_view(), name="list_students"), #post() delete() get() to handle multiple entities,
    path('student/<int:roll_no>', StudentModification.as_view(), name="student"), #get update delete single entity,
    path('subject/<str:subject>/', StudentSortedBy.as_view(), name="subject-marks"), #chemistry/, physics/, maths/,
    path('class_teacher/<str:teacher_name>/', SortByTeacher.as_view(), name="class_teacher"), 
    path('statics/<str:filtration>/', StudentMarkStatistic.as_view(), name="average_marks"), #average-marks/, report-failed/, top5/, teacher-analysis/
]