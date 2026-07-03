from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import (AllowAny,IsAuthenticated)
from .serializers import (RegisterSerializer,ProfileSerializer,ChangePasswordSerializer,ForgotPasswordSerializer)

class RegisterView(APIView):

    permission_classes = [AllowAny]

    def post(self, request):

        serializer = RegisterSerializer(
            data=request.data
        )

        if serializer.is_valid():
            serializer.save()

            return Response(
                {
                    "message": "User registered successfully"
                },
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
        
class ProfileView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        serializer = ProfileSerializer(
            request.user
        )

        return Response(serializer.data)        
    
class ChangePasswordView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):

        serializer = ChangePasswordSerializer(
            data=request.data
        )

        if serializer.is_valid():

            user = request.user

            old_password = serializer.validated_data[
                "old_password"
            ]

            new_password = serializer.validated_data[
                "new_password"
            ]

            if not user.check_password(
                old_password
            ):
                return Response(
                    {
                        "error":
                        "Old password is incorrect"
                    },
                    status=400
                )

            user.set_password(
                new_password
            )

            user.save()

            return Response(
                {
                    "message":
                    "Password changed successfully"
                }
            )

        return Response(
            serializer.errors,
            status=400
        )    
        
        
class ForgotPasswordView(APIView):

    permission_classes = [AllowAny]

    def post(self, request):

        serializer = ForgotPasswordSerializer(
            data=request.data
        )

        if serializer.is_valid():

            email = serializer.validated_data[
                "email"
            ]

            user_exists = User.objects.filter(
                email=email
            ).exists()

            if not user_exists:
                return Response(
                    {
                        "error":
                        "User not found"
                    },
                    status=404
                )

            return Response(
                {
                    "message":
                    "Password reset link sent"
                }
            )

        return Response(
            serializer.errors,
            status=400
        )        