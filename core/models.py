from django.db import models


# Create your models here.

class User(models.Model):
    name = models.CharField('Имя автора', max_length=128, null=True, blank=True)
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)

    def __str__(self):
        return f"{self.name} {self.pk}"


class Product(models.Model):
    name_product = models.CharField('Имя', max_length=128, null=True, blank=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    date_start = models.DateField("Дата старта продукта")
    cost = models.IntegerField(verbose_name='Стоимость')
    min_group_size = models.IntegerField(verbose_name='Максимум человек', null=True)
    max_group_size = models.IntegerField(verbose_name='Минимум человек', null=True)
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)

    def __str__(self):
        return f"{self.name_product} {self.pk}"


class Lesson(models.Model):
    name_lesson = models.CharField('Имя', max_length=128, null=True, blank=True)
    video_url = models.CharField(verbose_name='url', max_length=256, null=True, blank=True)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)


class Group(models.Model):
    name_group = models.CharField(verbose_name='Название группы', max_length=128, null=True, blank=True)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    amount_students = models.IntegerField(default=0)
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)


class RoleOfGroup(models.Model):
    name_role = models.CharField('Имя', max_length=128, null=True, blank=True)
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)


class UserToGroup(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    group_id = models.ForeignKey(Group, on_delete=models.CASCADE)
    role_id = models.ForeignKey(RoleOfGroup, on_delete=models.CASCADE)


class UserToProduct(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
