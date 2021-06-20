from django.db import models
from django.contrib.auth import get_user_model,authenticate
import uuid
import os



def recipe_image_file_path(instance,filename):
    """generate path for new image"""
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'

    return os.path.join('uploads/shop/',filename)





# Create your models here.
class Category(models.Model):
    """categories"""
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name



class Shop (models.Model):
        """shop model"""
        owner = models.OneToOneField(get_user_model(),related_name='shop_owner', on_delete=models. CASCADE)
        name = models.CharField(max_length=255)
        categories = models.ManyToManyField(Category,)
        address = models.CharField(max_length=400)
        image_url = models.ImageField(null=True,upload_to='')
        description = models.TextField(max_length=400)



        def __str__(self):
            return self.name


class ShopItem(models.Model):
    """shop items model"""
    name = models.CharField(max_length=300)
    price = models.FloatField(null=True,blank=True)
    description = models.TextField(max_length=255)
    image_url = models.ImageField(upload_to="")
    shop = models.ForeignKey(Shop,related_name='items', on_delete=models. CASCADE)
    category_item = models.ForeignKey(Category, on_delete=models. CASCADE)
    def __str__(self):
        return self.name




class FavItems(models.Model):

     shops = models.ForeignKey(Shop , related_name="user_fav" ,blank=True,on_delete=models. CASCADE)
     user = models.ForeignKey(get_user_model(),related_name='my_user', on_delete=models. CASCADE,blank=True)
     def __str__(self):
        return self.user.name


class Adv (models.Model):
        """advertisement model"""
        title = models.CharField(max_length=300)
        image_url = models.ImageField(upload_to="")

        def __str__(self):
            return self.title
