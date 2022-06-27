from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Product
from .serializers import ProductSerializer
from sparta.permissions import SellerPermission

from rest_framework import permissions, status
from django.utils import timezone
from django.db.models.query_utils import Q


class  ProductView(APIView): # CBV 방식
    permission_classes = [SellerPermission]

    # 상품 조회
    def get(self, request):
        time = timezone.now()
        if request.user.is_anonymous:
            query = Q(is_active=True) & Q(start_date__lt=time) & Q(end_date__gt=time)
        else:
            query = ( Q(is_active=True) & Q(start_date__lt=time) & Q(end_date__gt=time) ) | Q(author=request.user)
        products = Product.objects.filter(query)
        product_serializer = ProductSerializer(products, many=True).data
        print(product_serializer)

        return Response(product_serializer, status=status.HTTP_200_OK)

    # 상품 등록    
    def post(self, request):
        request.data['author'] = request.user.id
        product_serializer = ProductSerializer(data=request.data)

        if product_serializer.is_valid():
            product_serializer.save()
            return Response(product_serializer.data, status=status.HTTP_200_OK)
        
        return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    # 상품 수정
    def put(self, request, product_id):
        product = Product.objects.get(id=product_id)
        print(product)
        product_serializer = ProductSerializer(product, data=request.data, partial=True)

        if product_serializer.is_valid():
            product_serializer.save()
            return Response(product_serializer.data, status=status.HTTP_200_OK)
        
        return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 상품 삭제
    def delete(self, request, product_id):
        user = request.user.id
        product = Product.objects.get(id=product_id)
        # product_serializer = ProductSerializer(data=product)

        if product.author == user:
            product.delete()
            return Response({'message': 'delete method!!'}, status=status.HTTP_200_OK)

        return Response({'message': 'delete failed!!'}, status=status.HTTP_400_BAD_REQUEST)


class ReviewView(APIView):
    permission_classes = [permissions.AllowAny] 

    # 리뷰 조회
    def get(self, request):
        return Response({'message': 'get method!!'}, status=status.HTTP_200_OK)
        
    # 리뷰 작성
    def post(self, request):
        return Response({'message': 'post method!!'}, status=status.HTTP_200_OK)

    # 리뷰 수정
    def put(self, request):
        return Response({'message': 'put method!!'}, status=status.HTTP_200_OK)

    # 리뷰 삭제
    def delete(self, request):
        return Response({'message': 'delete method!!'}, status=status.HTTP_200_OK)