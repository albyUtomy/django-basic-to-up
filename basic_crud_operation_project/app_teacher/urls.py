from django.urls import path
from .views import (TeacherCreateListView, 
    GetUpdate_ID, 
    TeacherStudent, 
    TeacherAnalysis,
    BestTeacher,
    MakeInactiveView,
    ActiveOrInActive)


urlpatterns = [
    path('', TeacherCreateListView.as_view(), name="department-crud"),
    path('teacher/<int:teacher_id>/', GetUpdate_ID.as_view(), name="department-crud"),
    path('sort_students/<str:teacher_name>/', TeacherStudent.as_view(), name="class_teacher"), #get students details under specific teacher
    path('teacher_sort_a_z/', TeacherStudent.as_view(), name="class_teacher_sort"), #get students details sort by teacher
    path('teacher_report/',TeacherAnalysis.as_view(), name="teachers-report"),
    path('teacher_report/<str:teacher_name>/',TeacherAnalysis.as_view(), name="teacher-report"),
    path('best_teacher/', BestTeacher.as_view(), name='best-teacher'),
    path('teacher/<int:teacher_id>/make-inactive/', MakeInactiveView.as_view(), name='inactive'),
    path('teachers/<str:active_or_not>/', ActiveOrInActive.as_view(), name='active_inactive')
]