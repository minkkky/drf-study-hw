from unicodedata import category
from rest_framework import serializers
from .models import Product
from blog.models import Category, Article, Comment
from user.models import User, UserProfile
from rest_framework import status

class ProductSerializer(serializers.ModelSerializer):
   # 외래 키 관계로 이어져 있는 필드는 Serializer를 바로 호출할 수 있다.
   # hobby = HobbySerializer(many=True)

    class Meta:
        model = Product
        fields = "__all__"
