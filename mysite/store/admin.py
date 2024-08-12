from django.contrib import admin
from .models import *


class ProductPhotosInline(admin.TabularInline):
    model = ProductPhotos
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductPhotosInline

               ]


admin.site.register(Product,ProductAdmin)
admin.site.register(UserProfile)
admin.site.register(Category)
admin.site.register(Rating)
admin.site.register(Review)