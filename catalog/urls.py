from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.product_list, name='product-list'),
    path('products/<int:pk>/', views.product_detail, name='product-detail'),
    path('product/add/', views.product_create, name='product-create'),
    path('product/edit/<int:pk>',views.product_update, name='product-update'),
    path('product/delete/<int:pk>', views.product_delete, name='product-delete'),



    path('materials/', views.materials_list, name='material-list'),
    path('material/<int:pk>/', views.material_detail, name='material-detail'),
    path('material/add/', views.material_create, name='material-create'),
    path('material/edit/<int:pk>', views.material_update, name='material-update'),
    path('material/delete/<int:pk>', views.material_delete, name='material-delete'),




    path('categories/', views.category_list, name='category-list'),
    path('categories/<int:pk>/', views.category_detail, name='category-detail'),
    path('categories/add/', views.category_create, name='category-create'),
    path('categories/<int:pk>/edit/', views.category_update, name='category-update'),
    path('categories/<int:pk>/delete/', views.category_delete, name='category-delete'),


]