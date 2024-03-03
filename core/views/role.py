from rest_framework import viewsets, status
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response

from core.models import RoleOfGroup
from core.serializers import RoleSerializer


class AddRole(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = RoleSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class AllRoles(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        company = RoleOfGroup.objects.all()
        serializer = RoleSerializer(company, many=True)
        return Response(serializer.data)
