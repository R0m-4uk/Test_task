from django.urls import path, include
from rest_framework.routers import DefaultRouter

from core.views.user import AddUser, AllUsers
from core.views.product import AddProduct, AllProduct
from core.views.lesson import AddLesson, AllLessons
from core.views.group import AddGroup, AllGroups
from core.views.role import AddRole, AllRoles
from core.views.product_to_user import AddUserToProduct
from core.views.lesson_on_product import LessonOnProduct
from core.views.lessons_of_user import LessonsOfUser

router = DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),

    # user
    path("user/add/", AddUser.as_view(), name='add_user_api'),
    path("user/all/", AllUsers.as_view(), name='all_users_api'),
    path("user/add/product/", AddUserToProduct.as_view(), name='user_to_product'),
    path('users/<int:user_id>/products/<int:product_id>/lessons/', LessonsOfUser.as_view(), name='lessons_of_user'),

    # product
    path("product/add/", AddProduct.as_view(), name='add_product_api'),
    path("product/all/", AllProduct.as_view(), name='all_product_api'),
    path("product/lessons/count/", LessonOnProduct.as_view(), name='lessons_on_product'),

    # group
    path("group/add/", AddGroup.as_view(), name='add_group_api'),
    path("group/all/", AllGroups.as_view(), name='all_group_api'),


    # lesson
    path("lesson/add/", AddLesson.as_view(), name='add_lesson_api'),
    path("lesson/all/", AllLessons.as_view(), name='all_lesson_api'),


    # role
    path("role/add/", AddRole.as_view(), name='add_role_api'),
    path("role/all/", AllRoles.as_view(), name='all_role_api'),
]