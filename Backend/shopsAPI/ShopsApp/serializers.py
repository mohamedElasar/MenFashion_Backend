from rest_framework import serializers

from ShopsApp.models import Category,Shop,Adv,ShopItem,FavItems


class Cat_Serializer(serializers.ModelSerializer):
    """Serializer for category objects"""

    class Meta:
        model = Category
        fields = ('id', 'name')
        read_only_fields = ('id',)



class Items_Serializer(serializers.ModelSerializer):
        """Serializer for Shop items"""

        class Meta:
            model = ShopItem
            fields = ('name','price','description','image_url','category_item')
            read_only_fields = ('id',)




class Shop_Serializer(serializers.ModelSerializer):
    """Serializer for Shops"""
    items = Items_Serializer(many=True,)
    class Meta:
        model = Shop
        fields = ('id','owner', 'name','categories','address','image_url','description','items')
        read_only_fields = ('id',)



class Ad_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Adv
        fields = ('id', 'title', 'image_url')
        read_only_fields = ('id',)


class FavItems_Serializer(serializers.ModelSerializer):
    class Meta:
        model = FavItems
        fields = ('id','user', 'shops')
        read_only_fields = ('id',)



class ShopAdd_Serializer(serializers.ModelSerializer):
    """Serializer for Shops"""
    class Meta:
        model = Shop
        fields = ('id','name','categories','address','image_url','description','owner')
        read_only_fields = ('id','owner',)



class CreateItems_Serializer(serializers.ModelSerializer):
        """Serializer for Shop items"""

        class Meta:
            model = ShopItem
            fields = ('name','price','description','image_url','category_item')
            read_only_fields = ('id',)


class ShopImageAdd_Serializer(serializers.ModelSerializer):
    """Serializer for Shops"""
    class Meta:
        model = Shop
        fields = ('image_url',)
        read_only_fields = ('id',)
