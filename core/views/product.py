from rest_framework import viewsets, status
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response

from core.models import Product
from core.serializers import ProductSerializer


class AddProduct(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class AllProduct(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        company = Product.objects.all()
        serializer = ProductSerializer(company, many=True)
        return Response(serializer.data)

