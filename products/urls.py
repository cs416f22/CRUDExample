from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.view_products, name='view_products'),
    path('add', views.create_product, name='create_product'),
    path('update/<int:product_id>', views.update_product, name='update_product'),
    path('delete/<int:product_id>', views.delete_product, name='delete_product'),

]
