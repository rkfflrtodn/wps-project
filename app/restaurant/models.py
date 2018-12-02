from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


# Create your models here.
#
######################################
# Category : Restaurant   = 1 : N | M : N relations
# Shop : Item       = 1 : N

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    icon = models.ImageField(blank=True)
    is_public = models.BooleanField(default=False, db_index=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '카테고리'
        verbose_name_plural = f'{verbose_name} 목록'



class Restaurant(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
    )
    desc = models.TextField(blank=True)
    photo = models.ImageField(blank=True)
    is_public = models.BooleanField(default=False, db_index=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '식당'
        verbose_name_plural = f'{verbose_name} 목록'


class Review(models.Model):
    restaurant = models.ForeignKey(
        Restaurant,
        on_delete=models.CASCADE,
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    photo = models.ImageField(blank=True)
    rating = models.SmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.TextField()

    def __str__(self):
        return self.author


class Item(models.Model):
    restaurant = models.ForeignKey(
        Restaurant,
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=100, db_index=True)
    desc = models.TextField(blank=True)
    price = models.PositiveIntegerField()
    photo = models.ImageField(blank=True)
    is_public = models.BooleanField(default=False, db_index=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '아이템'
        verbose_name_plural = f'{verbose_name} 목록'


# class Order(models.Model):
#     pass