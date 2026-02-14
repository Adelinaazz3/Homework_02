from django.urls import path,admin
from .views import product_list
from .import views 
from product.views import product_detail_api_views


urlpatterns = [
    path('admin/', admin.site.urls),  
    path('', product_list, name='product-list'),
    path('<int:id>/', product_detail_api_views, name='product-detail'),
    path('products/<int:id>/', views.product_detail_api_view, name='product-detail'),
    path('api/v1/products/reviews/', views.products_with_views),



    path('categories/', views.category_list_api_view, name='category-list'),
    path('categories/<int:id>/', views.category_detail_api_view, name='category-detail'),
   


    path('reviews/', views.review_list_api_view, name='review-list'),
    path('reviews/<int:id>/', views.review_api_view, name='review-api'),

]
