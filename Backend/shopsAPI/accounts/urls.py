from django.urls import path
from accounts import views


app_name = 'accounts'

urlpatterns = [
    path('create/',views.CreateUserView.as_view(),name='create'),
    path('token/',views.CreateTokenView.as_view(),name='token'),
    path('owner/<int:pk>',views.CreateOwnerView.as_view(),name='owner')


]
