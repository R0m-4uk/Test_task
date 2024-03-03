from django.contrib import admin

# Register your models here.
from django.contrib import admin
from core.models import (User, Product, Group,
                         Lesson, RoleOfGroup, UserToProduct,
                         UserToGroup)


class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name_product', 'user_id', 'date_start', 'cost', 'min_group_size', 'max_group_size', 'created_at']

    def user_name(self, obj):
        return obj.user_id.get_full_name()

class GroupAdmin(admin.ModelAdmin):
    list_display = ['name_group', 'product_id', 'created_at']


class LessonAdmin(admin.ModelAdmin):
    list_display = ['name_lesson', 'video_url', 'product_id', 'created_at']


class RoleAdmin(admin.ModelAdmin):
    list_display = ['name_role', 'created_at']


class UserToProductAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'product_id']


class UserToGroupAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'group_id', 'role_id']


admin.site.register(User, UserAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(RoleOfGroup, RoleAdmin)
admin.site.register(UserToProduct, UserToProductAdmin)
admin.site.register(UserToGroup, UserToGroupAdmin)