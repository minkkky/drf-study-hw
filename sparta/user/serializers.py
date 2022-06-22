from unicodedata import category
from rest_framework import serializers
from blog.models import Category, Article, Comment
from user.models import User, UserProfile
from rest_framework import status

class UserProfileSerializer(serializers.ModelSerializer):
   # 외래 키 관계로 이어져 있는 필드는 Serializer를 바로 호출할 수 있다.
   # hobby = HobbySerializer(many=True)

    class Meta:
        model = UserProfile
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
   class Meta:
      model = Comment
      fields = "__all__"


class ArticleSerializer(serializers.ModelSerializer):
   category = serializers.SerializerMethodField()
   comment_set = CommentSerializer(many=True)

   def  get_category(self, obj):
      return [category.category for category in obj.category.all()]


   class Meta:
      model = Article
      fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
   # One-to-one 관계에서는 fk처럼 사용 가능하다.
   userprofile = UserProfileSerializer()
   article_set = ArticleSerializer(many=True)
   class Meta:
      # serializer에 사용될 model, field지정
      model = User
      # 모든 필드를 사용하고 싶을 경우 fields = "__all__"로 사용
      fields = ["username", "userprofile", "article_set"]

class UserSignupSerializer(serializers.ModelSerializer):
   class Meta:
      model = User
      fields = "__all__"

   def create(self, *args, **kwargs):
      user = super().create(*args, **kwargs)
      p = user.password
      user.set_password(p)
      user.save()
      return user

   def update(self, *args, **kwargs):
      user = super().create(*args, **kwargs)
      p = user.password
      user.set_password(p)
      user.save()

      return user