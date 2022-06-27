from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator
from sorl.thumbnail import get_thumbnail
from django.utils.html import format_html

class Product(models.Model):
    author = models.ForeignKey('user.User', on_delete=models.CASCADE)
    title = models.CharField("상품이름", max_length=50)
    thumbnail = models.ImageField("상품사진" )
    @property
    def thumbnail_preview(self):
        if self.thumbnail:
            _thumbnail = get_thumbnail(self.thumbnail,
                                   '150x150',
                                   upscale=False,
                                   crop=False,
                                   quality=100)
            return format_html('<img src="{}" width="{}" height="{}">'.format(_thumbnail.url, _thumbnail.width, _thumbnail.height))
        return ""
    desc = models.TextField("상품설명")
    created_at = models.DateTimeField(auto_now_add=True)
    start_date = models.DateField("노출 시작 일자", default=timezone.now)
    end_date = models.DateField("노출 종료 일자", default=timezone.now)
    price = models.IntegerField(default=0)
    is_active = models.BooleanField("활성화 여부", default=True)


    def __str__(self):
        return f'{self.title} ({self.author}) : {self.price}원'

class Review(models.Model):
    # 작성자, 상품, 내용, 평점, 작성일
    author = models.ForeignKey('user.User', on_delete=models.CASCADE)
    title = models.ForeignKey('product.Product', on_delete=models.CASCADE)
    content = models.TextField("리뷰내용")
    star = models.IntegerField("별점", default=0, validators=[MinValueValidator(0), MaxValueValidator(10)])
    reviewed_date = models.DateTimeField(auto_now_add=True)