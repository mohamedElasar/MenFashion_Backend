from django.contrib import admin
from ShopsApp import models

admin.site.register(models.Category)
admin.site.register(models.Adv)
admin.site.register(models.FavItems)
# admin.site.register(models.ShopOwner)



class ItemsInline(admin.StackedInline):
    model = models.ShopItem



class ShopAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,{'fields': ['owner','name','categories','address','image_url','description']}),
    ]
    inlines = [ItemsInline]

admin.site.register(models.Shop, ShopAdmin)
