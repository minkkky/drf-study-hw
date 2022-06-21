from re import T
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from .models import Article, Category
from sparta.permissions import RegistedMoreThanTreeDaysUser, IsAdminOrAuthenticateReadOnly
from rest_framework import status
from user.serializers import ArticleSerializer
from django.utils import timezone

# Create your views here.
class BlogView(APIView):
    permission_classes = [IsAdminOrAuthenticateReadOnly]

    def get(self, request):
        today = timezone.now()
        articles = Article.objects.filter(
            author=request.user,
            exposure_start_date__lte=today,
            exposure_end_date__gte=today
            ).order_by('-id')
        # titles = [ article.title for article in articles ]
        serializer = ArticleSerializer(articles, many=True).data
        return Response(serializer, status=status.HTTP_200_OK)
    
    def post(self, request):
        author = request.user
        title = request.data.get('title', '')
        category = request.data.pop('category', [])
        content = request.data.get('content', '')

        if len(title) <= 5:
            return Response({"message": "게시글을 작성할 수 없어요! (제목은 5자 이상)"}, status=status.HTTP_400_BAD_REQUEST)

        if len(content) <= 20:
            return Response({"message": "게시글을 작성할 수 없어요! (내용은 20자 이상)"}, status=status.HTTP_400_BAD_REQUEST)

        if not category:
            return Response({'message': '카테고리를 지정해주세요!'}, status=status.HTTP_400_BAD_REQUEST)

        new_article = Article(
            author=author, 
            **request.data
            )
        new_article.save()
        new_article.category.add(*category)
        return Response({"message": "게시물 작성완료!"}, status=status.HTTP_200_OK)