from django.db import models
from django.utils import timezone

class Product(models.Model):
    author = models.ForeignKey('user.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    thumbnail = models.ImageField("상품사진" )
    desc = models.TextField("상품설명")
    created_at = models.DateTimeField(auto_now_add=True)
    exposure_start_date = models.DateField("노출 시작 일자", default=timezone.now)
    exposure_end_date = models.DateField("노출 종료 일자", default=timezone.now)

    # def __str__(self):
    #     return f'{self.title} ({self.author})'