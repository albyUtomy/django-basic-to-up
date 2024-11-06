from django.urls import path
from .views import CreateUserView, LoginView, LogoutView

urlpatterns = [
    path('create-user/', CreateUserView.as_view(), name='create_user'),
    path('login-user/', LoginView.as_view(), name='create_user'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
