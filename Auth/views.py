from rest_framework.decorators import api_view,permission_classes
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.decorators import authentication_classes,permission_classes
from rest_framework.authentication import SessionAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.utils import timezone
from drf_yasg.utils import swagger_auto_schema
from .serializers import UserSerializer


@swagger_auto_schema(
    method='post',
    request_body=UserSerializer,
    responses={
        200: 'User registered succesfully',
        400: 'Bad request'
    },
    security=[],
    operation_summary="User register",
    operation_description="This view allows you to register a new user.",
)
@api_view(['POST'])
@permission_classes([])
def register(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        user = User.objects.get(username=request.data['username'])
        user.set_password(request.data['password'])
        user.save()
        token = Token.objects.create(user=user)
        return Response({'token': token.key, 'user':serializer.data})
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(
    method='post',
    request_body=UserSerializer,
    responses={
        200: 'User authentication succesfully',
        400: 'Bad request'
    },
    security=[],
    operation_summary="User login",
    operation_description="This view allows you to login a  uregistered ser.",
)
@api_view(['POST'])
def login(request):
    user = get_object_or_404(User,username=request.data['username'])
    if not user.check_password(request.data['password']):
        return Response({'detail':'Not found'},status=status.HTTP_400_BAD_REQUEST)
    token = Token.objects.get_or_create(user=user)
    serializer = UserSerializer(user)
    return Response({'token': token.key})


@swagger_auto_schema(
    method='get',
    responses={
        200: 'User token validated succesfully',
        400: 'Bad request'
    },
    security=[],
    operation_summary="Test validity of a user token",
    operation_description="This view allows to a user check the token's validity.",
)
@api_view(['GET'])
@authentication_classes([SessionAuthentication,TokenAuthentication])
@permission_classes([IsAuthenticated])
def test_token(request):
    token = Token.objects.get(user=request.user)
    token_age = timezone.now() - token.created
    return Response({'detail':'Token is valid', 'token_age': str(token_age)})

@swagger_auto_schema(
    method='post',
    responses={
        200: 'User logged out succesfully',
        400: 'Bad request'
    },
    security=[],
    operation_summary="Logout a user",
    operation_description="This view allows to a registered user logged out.",
)
@api_view(['POST'])
@authentication_classes([SessionAuthentication,TokenAuthentication])
@permission_classes([IsAuthenticated])
def logout(request):
    token = Token.objects.get(user=request.user)
    token.delete()
    return Response(status=status.HTTP_200_OK)