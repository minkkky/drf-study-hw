from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Product as ProductModel
from .serializers import ProductSerializer

from rest_framework import permissions, status
from django.utils import timezone


class  ProductView(APIView): # CBV 방식

    # 상품 조회
    def get(self, request):
        return Response({'message': 'get method!!'})

    # 상품 등록    
    def post(self, request):
        request.data['author'] = request.user.id
        product_serializer = ProductSerializer(data=request.data)

        if product_serializer.is_valid():
            product_serializer.save()
            return Response({"message": "정상"}, status=status.HTTP_200_OK)
        
        return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


        # user = request.user
        # print(request.data)
        # data = ProductModel(
        #     author=user, 
        #     **request.data
        # )
        # print(data)
        # data.save()
        # serialized_product_data = ProductSerializer(Many=True).data

        # return Response(data, status=status.HTTP_200_OK)
        # return Response({'message': 'post method!!'})

    # 상품 수정
    def put(self, request, ):
        return Response({'message': 'put method!!'})

    # 상품 삭제
    def delete(self, request):
        return Response({'message': 'delete method!!'})
