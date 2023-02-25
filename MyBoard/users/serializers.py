from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password

from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.validators import UniqueValidator


class RegisterSerializer(serializers.ModelSerializer):
    """회원가입용 시리얼라이저 클래스.
    user_name, email, password, password2가 있다."""

    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())],
    )
    password = serializers.CharField(
        required=True,
        write_only=True,
        validators=[validate_password],
    )
    password2 = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'password2', 'email']

    def validate(self, data):
        """비밀번호 두 개(password, password2)가 일치하는지 확인한다."""
        if data['password'] != data['password2']:
            raise serializers.ValidationError(
                {"password": "password fields didn't match"}
            )
        return data

    def create(self, validated_data):
        """검증된 정보로 회원 하나를 생성한다."""
        user = User(  # 책에서는 'User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        token = Token.objects.create(user=user)
        return user


class LoginSerializer(serializers.Serializer):
    """로그인용 시리얼라이저 클래스.
    로그인은 모델과 관련이 없기 때문에 ModelSerializer를 쓰지 않는다."""

    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user:
            token = Token.objects.get(user=user)
            return token
        raise serializers.ValidationError(
            {"error": "Unable to log in with provided credentials."})
