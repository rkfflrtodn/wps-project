from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


# Create your models here.
#
######################################
# Category : Shop   = 1 : N | M : N relations
# Shop : Item       = 1 : N

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    icon = models.ImageField(blank=True)
    is_public = models.BooleanField(default=False, db_index=True)
    pass


class Restaurant(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    category = models.ForeignKey(Category)
    desc = models.TextField(blank=True)
    photo = models.ImageField(blank=True)
    is_public = models.BooleanField(default=False, db_index=True)
    pass


class Review(models.Model):
    restaurant = models.ForeignKey(Restaurant)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    photo = models.ImageField(blank=True)
    rating = models.SmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.TextField()


class Item(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    desc = models.TextField(blank=True)
    price = models.PositiveIntegerField()
    photo = models.ImageField(blank=True)
    is_public = models.BooleanField(default=False, db_index=True)
    pass



# class Order(models.Model):
#     pass