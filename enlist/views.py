from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from knox.serializers import UserSerializer

HTTP_422_UNPROCESSABLE_ENTITY = 422

class RegisterView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, format=None):
        data = request.data

        username = request.data.get('username')
        email = request.data.get('email')
        password1 = request.data.get('password1')
        password2 = request.data.get('password2')

        passwords_match = self.check_password(password1, password2)
        self.check_email(email)

        user = self.create_user(username, email, password1)
        self.send_confirmation_email(email)

        return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)

class RegistrationConfirmationView(APIView):
    permission_classes = (AllowAny,)
'''
class PasswordResetView(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
'''
