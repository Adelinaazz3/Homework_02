from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import  Product
from .serializers import  (
    ProductSerializer,
    ProductDetailSerializer,
    CategorySerializer,
    CategoryDetailSerializer,
    ReviewSerializer,
    ReviewDetailSerializer
)

@api_view(['GET'])
def product_detail_api_view(request, id):
    product = Product.objects.get(id=id)
    data = ProductDetailSerializer(product, many=False).data

    return Response(
        data=data,
    )




@api_view(['GET'])
def product_list_api_view(request):
    product=Product.objects.all()
    data = ProductSerializer(product, many=True).data

    return Response(
        data=data,
    )





@api_view(['GET'])
def category_list_api_view(request):
    category= Category.objects.all()
    data = CategorySerializer(category, many=True).data

    return Response(
        data=data,
    )

    
@api_view(['GET'])   
def category_detail_api_view(request, id):
    category=Category.objects.get(id=id)
    data=CategoryDetailSerializer(category, many=False).data

    return Response(
        data=data,  
    )



@api_view(['GET'])
def review_list_api_view(request):
    review=Review.objects.all()
    data = ReviewSerializer(review, many=True).data

    return Response(
        data=data,
    )

@api_view(['GET'])
def review_detail_api_view(request, id):
    review=Review.objects.get(id=id)
    data=ReviewDetailSerializer(review, many=False).data

    return Response(
        data=data,
    )