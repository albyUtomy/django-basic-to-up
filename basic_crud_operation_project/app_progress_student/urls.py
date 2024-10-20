
from django.urls import path, include
from .views import StudentCrudOperation,StudentMarkFiltration, StudentModification, StudentSortedBy

urlpatterns = [
    path('', StudentCrudOperation.as_view(), name="list_students"),
    path('student/<int:roll_no>', StudentModification.as_view(), name="student"),
    path('subject/<str:para_url>/', StudentSortedBy.as_view(), name="chemistry-marks"),
    path('class_teacher/', StudentSortedBy.as_view(), name="chemistry-marks"),
    path('class_teacher/<str:para_url>/', StudentSortedBy.as_view(), name="class_teacher"),
    path('subject/average-list/', StudentMarkFiltration.as_view(), name="chemistry_avg"),
]