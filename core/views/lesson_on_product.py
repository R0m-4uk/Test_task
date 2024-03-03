from django.utils import timezone
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from core.models import Product
from core.serializers import LessonsOnProductSerializer


class LessonOnProduct(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        product = Product.objects.order_by('date_start').filter(date_start__gt=timezone.now())
        seializer = LessonsOnProductSerializer(product, many=True)
        return Response(seializer.data)