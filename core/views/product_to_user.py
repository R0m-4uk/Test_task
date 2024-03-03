from django.utils import timezone

from core.models import User, Product
from rest_framework import viewsets, status
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from core.models import UserToGroup, Group
from django.shortcuts import get_object_or_404
from core.serializers import UserToProductSerializer


class AddUserToProduct(APIView):
    permission_classes = [permissions.AllowAny]

    def get_group(self, product_id):
        groups = Group.objects.filter(product_id__id=product_id)
        product = Product.objects.get(id=product_id)
        if len(groups) == 0:
            group = Group.objects.create(product_id=product)
            print(group)


    def post(self, request):
        serializer = UserToProductSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        product_id = serializer.data.get('product_id')
        group = self.get_group(product_id)
        print(group)
        # serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

