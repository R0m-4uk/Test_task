from rest_framework import status
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from core.serializers import UserToGroupSerializer


class AddUserToGroup(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = UserToGroupSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
