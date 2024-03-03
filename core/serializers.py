from rest_framework import serializers
from core.models import Product, User, Lesson, Group, RoleOfGroup, UserToGroup, UserToProduct


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoleOfGroup
        fields = '__all__'


class UserToProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserToProduct
        fields = '__all__'


class UserToGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserToGroup
        fields = '__all__'


class LessonsOnProductSerializer(serializers.ModelSerializer):
    lessons_count = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ('name_product', 'user_id', 'date_start',
                  'cost', 'min_group_size', 'max_group_size',
                  'created_at', 'lessons_count')

    def get_lessons_count(self, obj):
        return obj.lesson_set.count()
