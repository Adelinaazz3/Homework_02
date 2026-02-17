from django.urls import path
from . import views

urlpatterns = [

    path('api/products/', views.product_list_api_view, name='product-list'),
    path('api/products/<int:1>/', views.product_detail_api_view, name='product-detail'),
   
    path('api/v1/products/reviews/', views.products_with_views),
    path('api/categories/', views.category_list_api_view, name='category-list'),
    path('api/categories/<int:2>/', views.category_detail_api_view, name='category-detail'),
   
    path('api/reviews/', views.review_list_api_view, name='review-list'),
    path('api/reviews/<int:3>/', views.review_detail_api_view, name='review-detail'),
]

