from django.contrib import admin

# Register your models here.
from django.contrib import admin
from core.models import (User, Product, Group,
                         Lesson, RoleOfGroup, UserToProduct,
                         UserToGroup)


class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'user', 'date_start', 'cost', 'min_group_size', 'max_group_size', 'created_at']

    def user_name(self, obj):
        return obj.user_id.get_full_name()


class GroupAdmin(admin.ModelAdmin):
    list_display = ['name', 'product', 'created_at']


class LessonAdmin(admin.ModelAdmin):
    list_display = ['name', 'video_url', 'product', 'created_at']


class RoleAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']


class UserToProductAdmin(admin.ModelAdmin):
    list_display = ['user', 'product']


class UserToGroupAdmin(admin.ModelAdmin):
    list_display = ['user', 'group', 'role']


admin.site.register(User, UserAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(RoleOfGroup, RoleAdmin)
admin.site.register(UserToProduct, UserToProductAdmin)
admin.site.register(UserToGroup, UserToGroupAdmin)
