from rest_framework import serializers
from .models import Product, Review
from blog.models import Category, Article, Comment
from user.models import User, UserProfile
from rest_framework import status
from django.utils import timezone
from django.db.models import Avg
from django.forms import model_to_dict

class ReviewSerializer(serializers.ModelSerializer):
   class Meta:
      model = Review
      fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    
    # author = serializers.SlugRelatedField(
    #     read_only=True,
    #     slug_field='username'
    # )

    newest_review = serializers.SerializerMethodField()
    avg_star = serializers.SerializerMethodField()

    def get_newest_review(self, obj):
        newest_review = obj.review_set.all().order_by('-reviewed_date').first()
        # newest_review = dict(obj.review_set.all().order_by('-reviewed_date').first())
        return model_to_dict(newest_review)
        # return newest_review

    def get_avg_star(self, obj):
        reiviews = obj.review_set.all()
        if reiviews.count() == 0:
            return 0
        # avg_star = reiviews.aggregate(Avg('star'))
        # avg_star = dict(reiviews.aggregate(avg_star=Avg('star'))['avg_star'])
        # return model_to_dict(avg_star)
        # return json.dumps(avg_star)
        # return reiviews.aggregate(avg_star=Avg('star'))
        return reiviews.aggregate(avg_star=Avg('star'))['avg_star']


    def validate(self, data):
        start_date = data.get('start_date')
        end_date = data.get('end_date')

        if not end_date:
            raise serializers.ValidationError(
                    detail={"error": "종료 일자를 입력하세요."},
                )

        if end_date < timezone.now().date():
            raise serializers.ValidationError(
                        detail={"error": "종료 일자는 과거일 수 없습니다."},
                    )

        if end_date < start_date:
            raise serializers.ValidationError(
                        detail={"error": "종료 일자는 시작 일자보다 과거일 수 없습니다."},
                    )

        return data

    def create(self, validated_data):
        desc = validated_data.pop('desc') + f'\n{timezone.now().date()}에 등록된 상품입니다.'
        validated_data['desc'] = desc

        product = Product(**validated_data)
        product.save()

        return product

    def update(self, instance, validated_data):

        instance.title = validated_data.get('title')
        instance.thumbnail = validated_data.get('thumbnail')
        instance.desc = validated_data.get('desc') + f'\n\n{timezone.now()}에 수정되었습니다.'
        instance.start_date = validated_data.get('start_date')
        instance.end_date = validated_data.get('end_date')
        instance.price = validated_data.get('price')
        instance.is_active = validated_data.get('is_active')

        instance.save()

        return instance

    class Meta:
        model = Product
        fields = "__all__"
