"""
URL configuration for shop_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.http import HttpResponse
from django.contrib import admin
from django.urls import path, include
from product.views import(
    product_list_api_view,
    product_detail_api_view,
    category_list_api_view,
    category_detail_api_view,
    review_list_api_view,
    review_detail_api_view,
    

)


def home(request):
    return HttpResponse('Hello, World!')

   
urlpatterns = [
   
   path('admin/', admin.site.urls),
   
   
    path('products/', product_list_api_view, name='product-list'),
    path('products/<int:id>/', product_detail_api_view, name='product-detail'),
    path('', home, name='home'),



    path('categories/', category_list_api_view, name='category-list'),
    path('categories/<int:id>/', category_detail_api_view, name='category-detail'),
    path('', home, name='home'),



    path('reviews/', review_list_api_view, name='review-list'),
    path('reviews/<int:id>/', review_detail_api_view, name='review-detail'),
    path('', home , name='home'),

] 
