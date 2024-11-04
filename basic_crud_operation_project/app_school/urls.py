from django.urls import path
from .views import SchoolCrud, SchoolCrudById, Filtration, MakeInActive, ActiveOrInActive


urlpatterns = [
    path('', SchoolCrud.as_view(), name="school-crud"),
    path('<int:school_id>/', SchoolCrudById.as_view(), name="school-crud"),
    # path('school_details/<int:school_id>/',SchoolUpdateRetrieveView.as_view(), name='school-update-retrieve'),
    path('school/departments/<int:school_id>', Filtration.as_view(), name='school_departments'),
    path('school/teachers/<int:school_id>', Filtration.as_view(), name='teacher_name'),
    path('school/students/<int:school_id>', Filtration.as_view(), name='school_students'),
    path('school/<int:school_id>/make-inactive/', MakeInActive.as_view(), name='make_inactive'),
    path('schools/<str:active_or_not>/', ActiveOrInActive.as_view(), name='active_inactive')
    ]