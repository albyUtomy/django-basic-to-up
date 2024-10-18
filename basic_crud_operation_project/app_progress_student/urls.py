
from django.urls import path, include
from .views import StudentCrudOperation, StudentModification, StudentSortedBy

urlpatterns = [
    path('', StudentCrudOperation.as_view(), name="list_students"),
    path('student/<int:roll_no>', StudentModification.as_view(), name="student"),
    path('chemistry-mark-list/', StudentSortedBy.as_view(), name="chemistry-marks"),
    path('physics-mark-list/', StudentSortedBy.as_view(), name="physics-marks"),
    path('maths-mark-list/', StudentSortedBy.as_view(), name="maths-marks"),
    path('sort-by-class_teacher/', StudentSortedBy.as_view(), name="chemistry-marks"),
    path('class_teacher/<str:para_url>/', StudentSortedBy.as_view(), name="class_teacher")
]