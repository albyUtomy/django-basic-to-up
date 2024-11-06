
from django.contrib.auth.hashers import check_password, make_password
from django.contrib.auth import authenticate, get_user_model
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .serializers import LoginSerializer, CustomUserSerializer



# User = get_user_model()

class LoginView(APIView):
    """
    API View for user login that returns an authentication token.
    """
    def post(self, request):
        try:
            serializer = LoginSerializer(data=request.data)
            serializer.is_valid()

            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            print(">>>>>>> password : ", password)

            hashed_password_from_database = "pbkdf2_sha256$870000$I3hot6MWOBFrLcYhE6Glrj$XVdQMZVECrMBYhRPEP887k3cHWnjH9MSkTonMOMAI04="
            if check_password(password,hashed_password_from_database):
                print("Password matches the hash from the database")
            else:
                print("Password does not match the hash from the database")

            # Authenticate the user
            user = authenticate(request, username=username, password=password)
            print(">>>>> user : ",user)

            if user is not None:
                # Generate or retrieve the token for the authenticated user
                token, created = Token.objects.get_or_create(user=user)
                print(">>>>>token type :",token)
                return Response({
                    "token": token.key,
                    "message": "Login successful."
                }, status=status.HTTP_200_OK)
            else:
                return Response(
                    {"error": "Invalid username or password"},
                    status=status.HTTP_400_BAD_REQUEST
                )
        except Exception as e:
            print("Error during login:", e)
            return Response({"error": "An error occurred during login", 'error':str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]  # Ensure the user is authenticated

    def post(self, request):
        try:
            # Retrieve the token of the authenticated user
            token = Token.objects.get(user=request.user)
            token.delete()  # Delete the token to log the user out
            return Response({"message": "Successfully logged out."}, status=status.HTTP_200_OK)
        except Token.DoesNotExist:
            return Response({"error": "Token not found."}, status=status.HTTP_400_BAD_REQUEST)


class CreateUserView(APIView):
    """
    API View to create a new user.
    """

    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({
                "user_id": user.id,
                "username": user.username,
                "email": user.email,
                "message": "User created successfully."
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





# class LoginView(APIView):
#     """
#     API View for user login that returns an authentication token.
#     """
#     def post(self, request):
#         serializer = LoginSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)

#         username = serializer.validated_data['username']
#         password = serializer.validated_data['password']

#         try:
#             # Authenticate the user
#             user = authenticate(request, username=username, password=password)

#             if user is not None:
#                 # Generate or retrieve the token for the authenticated user
#                 token, created = Token.objects.get_or_create(user=user)
#                 return Response({
#                     "token": token.key,
#                     "message": "Login successful."
#                 }, status=status.HTTP_200_OK)
#             else:
#                 # Specific message for invalid credentials
#                 return Response(
#                     {"error": "Invalid username or password"},
#                     status=status.HTTP_400_BAD_REQUEST
#                 )

#         except Exception as e:
#             # Catch any unexpected errors
#             return Response(
#                 {"error": "An error occurred. Please try again later."},
#                 status=status.HTTP_500_INTERNAL_SERVER_ERROR
#             )