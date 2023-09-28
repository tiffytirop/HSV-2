from django.urls import path
from property import views

urlpatterns = [
    path('property_single/', views.property_single, name='property_single'),
    path('property_grid/', views.property_grid, name='property_grid'),
    path('display_images/', views.display_images, name='display_images'),
    path('upload_image/', views.upload_image, name='upload_image'),

]