from django.db.models import QuerySet
from django.utils import timezone

from core.models import User, Product, UserToProduct
from rest_framework import viewsets, status
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from core.models import UserToGroup, Group
from django.shortcuts import get_object_or_404
from core.serializers import UserToProductSerializer
from core.service.group import get_new_name_group
from core.service.role import get_user_role


class AddUserToProduct(APIView):
    permission_classes = [permissions.AllowAny]

    def get_group(self, product):
        groups: QuerySet = Group.objects.filter(product=product).order_by('-amount_students')
        print(product.max_group_size, groups)
        last_index = len(groups) - 1
        if len(groups) == 0 or groups[last_index].amount_students == product.max_group_size:
            group: Group = Group.objects.create(product=product)
            group.name = get_new_name_group(group)
            group.save()
            return group
        return groups[last_index]

    def post(self, request):
        serializer = UserToProductSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        role = get_user_role()
        if role is None:
            return Response({'message': 'Такой роли не существует'}, status=status.HTTP_400_BAD_REQUEST)

        user = serializer.validated_data.get('user')
        product = serializer.validated_data.get('product')
        if len(UserToProduct.objects.filter(user=user, product=product)) > 0:
            return Response({'message': 'Пользователь уже добавлен в продукт'}, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()

        group = self.get_group(product)
        print(group)
        UserToGroup.objects.create(user=user, group=group, role=role)
        group.amount_students += 1
        group.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
