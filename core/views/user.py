from rest_framework import viewsets, status
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response

from core.models import User
from core.serializers import UserSerializer


class AddUser(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class AllUsers(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        company = User.objects.all()
        serializer = UserSerializer(company, many=True)
        return Response(serializer.data)
