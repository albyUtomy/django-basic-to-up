from django.urls import path
from .views import TeacherCreateListView, TeacherUpdateDestroy


urlpatterns = [
    path('', TeacherCreateListView.as_view(), name="department-crud"),
    path('teacher_details/<int:teacher_id>/', TeacherUpdateDestroy.as_view(), name="department-crud"),
]