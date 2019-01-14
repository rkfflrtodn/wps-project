from urllib.parse import quote
from django.contrib import admin

# Register your models here.
from django.utils.safestring import mark_safe

from .models import Category, Restaurant, Item



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['icon_img', 'name']
    list_display_links = ['name']
    search_fields = ['name']

    def icon_img(self, category):
        if category.icon:
            img_tag = '<img src="{}" style="max-width: 72px;" />'
            return mark_safe(img_tag.format(category.icon.url))
        return None


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'address_link')


    def address_link(self, restaurant):
        if restaurant.address:
            # url = 'https://map.naver.com/?query=' + quote(restaurant.address)
            url = 'https://www.google.com/maps/place/' + quote(restaurant.latlng)
            # url = 'https://www.google.com/maps/place/' + quote(restaurant.address)
            return mark_safe('<a href="{}" target="_blank">{}</a>'.format(url, restaurant.address))
        return None
    address_link.short_description = '주소'


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['restaurant', 'name']
    list_display_links = ['name']
    list_filter = ['restaurant']
    search_fields = ['name']