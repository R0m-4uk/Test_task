from core.models import User, Product
from rest_framework import viewsets, status
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from core.models import UserToProduct, Lesson
from django.shortcuts import get_object_or_404
from core.serializers import LessonSerializer


class LessonsOfUser(APIView):
    permission_classes = [permissions.AllowAny]
    serializer = LessonSerializer

    def get(self, request, user_id, product_id):
        # Получаем пользователя по user_id
        user = get_object_or_404(User, pk=user_id)

        # Проверяем доступ пользователя к продукту
        get_object_or_404(UserToProduct, user_id=user, product_id=product_id)

        # Получаем список уроков для данного продукта
        lessons = Lesson.objects.filter(product_id=product_id)

        # Сериализуем и возвращаем список уроков
        serializer = LessonSerializer(lessons, many=True)
        return Response(serializer.data)