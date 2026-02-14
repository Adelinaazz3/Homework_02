from django.db.models import Avg,Count
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import  Product,Category,Review
from .serializers import  (
    ProductWithReviewsSerializer,
    CategorySerializer,
    ReviewSerializer

)

@api_view(['GET'])
def product_detail_api_view(request, id):
    product = Product.objects.prefetch_related('reviews').get(id=id)
    serializer = ProductWithReviewsSerializer(product)

    return Response(serializer.data,
    )

@api_view(['GET'])
def product_list_api_view(request):
    products = Product.objects.prefetch_related('reviews').annotate(
        rating=Avg('reviews__stars')
    )
    serializer = ProductWithReviewsSerializer(products, many=True)
    return Response(serializer.data)




@api_view(['GET'])
def category_list_api_view(request):
    categories = Category.objects.annotate(
        products_count=Count('products')
    )
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def category_detail_api_view(request, id):
    category = Category.objects.get(id=id)
    serializer = CategorySerializer(category)
    return Response(serializer.data)



@api_view(['GET'])
def review_list_api_view(request):
    reviews = Review.objects.all()
    serializer = ReviewSerializer(reviews, many=True)
    return Response(serializer.data)
    
@api_view(['GET'])
def review_detail_api_view(request, id):
    review = Review.objects.get(id=id)
    serializer = ReviewSerializer(review)
    return Response(serializer.data)


