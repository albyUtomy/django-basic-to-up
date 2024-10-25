from django.urls import path
from .views import SchoolCrud


urlpatterns = [
    path('', SchoolCrud.as_view(), name="school-crud"),
    ]