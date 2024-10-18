from django.urls import path
from .views import StudentView, StudentByID

urlpatterns = [
    path("", StudentView.as_view(), name="student"),
    path("getby_id/<int:p_id>", StudentByID.as_view(), name="list_student"),
]
