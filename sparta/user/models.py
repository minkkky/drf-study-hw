from django.db import models

class User(models.Model):
    class Meta:
        db_table: "user"

    username = models.CharField(max_length=20)
    password = models.CharField(max_length=300)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    birth = models.DateField()
    date_joined = models.DateTimeField(auto_now=True)