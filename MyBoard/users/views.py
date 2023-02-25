from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import generics, status

from .serializers import RegisterSerializer, LoginSerializer


class RegisterView(generics.CreateAPIView):
    """회원가입용 뷰 클래스. generics로 구현.
    Create 기능만 필요하므로 CRUD를 한꺼번에 다 지원하는 ViewSet을 쓸 필요가 없다."""

    queryset = User.objects.all()
    serializer_class = RegisterSerializer


class LoginView(generics.GenericAPIView):
    """로그인용 뷰 클래스."""

    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        token = serializer.validated_data
        return Response({'token': token.key}, status=status.HTTP_200_OK)
