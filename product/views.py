from django.db.models import Avg, Count
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product, Category, Review
from rest_framework import status
from .serializers import (
    ProductWithReviewsSerializer,
    CategorySerializer,
    ReviewSerializer
)


@api_view(['GET'])
def product_detail_api_view(request, id):
    product = Product.objects.prefetch_related('reviews').get(id=id)
    serializer = ProductWithReviewsSerializer(product)
    return Response(serializer.data)


@api_view(['GET'])
def product_list_api_view(request):
    products = Product.objects.prefetch_related('reviews').annotate(
        rating=Avg('reviews__stars')
    )
    serializer = ProductWithReviewsSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST','PUT', 'DELETE'])
def category_list_api_view(request):
    categories = Category.objects.annotate(
        products_count=Count('products')
    )

    if request.method == 'GET':
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def category_detail_api_view(request, id):
    try:
        category = Category.objects.get(id=id)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = CategorySerializer(category)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def review_list_api_view(request):
    if request.method == 'GET':
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
         data = request.data.copy()
         data['user'] = request.user.id
    if 'product' not in data:
         return Response({"error": "Поле 'product' обязательно"}, status=400)

    serializer = ReviewSerializer(data=data)
    if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def review_detail_api_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def product_list_api_view(request):
    if request.method == 'GET':
        products = Product.objects.prefetch_related('reviews').annotate(
            rating=Avg('reviews__stars')
        )
        serializer = ProductWithReviewsSerializer(products, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProductWithReviewsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def product_detail_api_view(request, id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProductWithReviewsSerializer(product)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ProductWithReviewsSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['GET', 'PUT', 'DELETE'])
def category_detail_api_view(request, id):
    try:
        category = Category.objects.get(id=id)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
