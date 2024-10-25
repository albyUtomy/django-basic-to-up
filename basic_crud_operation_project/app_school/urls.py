from django.urls import path
from .views import SchoolCrud, SchoolUpdateRetrieveView


urlpatterns = [
    path('', SchoolCrud.as_view(), name="school-crud"),
    path('school_details/<int:school_id>/',SchoolUpdateRetrieveView.as_view(), name='school-update-retrieve')
    ]