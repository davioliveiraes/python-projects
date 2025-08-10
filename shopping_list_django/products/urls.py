from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
   path('', views.products_list, name='list'),
   path('add/', views.add_product, name='add'),
   path('toggle/<int:product_id>/', views.toggle_purchased, name='toggle'),
   path('delete/<int:product_id>/', views.delete_product, name='delete'),
   path('update-quantity/<int:product_id>/', views.update_quantity, name='update_quantity'),
]
