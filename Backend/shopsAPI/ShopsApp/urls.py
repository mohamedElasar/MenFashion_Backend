from django.urls import path, include
from rest_framework.routers import DefaultRouter

from ShopsApp import views


router = DefaultRouter()
router.register('categories', views.Cat_ViewSet)
router.register('shops', views.Shop_ViewSet)
router.register('adv', views.Adv_ViewSet)
router.register('favorits', views.Favs_ViewSet)
router.register('shops/add', views.AddShop_ViewSet)
router.register('shops/img', views.AddShopImage_ViewSet)

router.register('items/add', views.AddItem_ViewSet)





app_name = 'api'

urlpatterns = [
    path('', include(router.urls)),
    # path('favorits/',views.Favs_ViewSet.as_view())
]
