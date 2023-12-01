from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Profile(models.Model):
    # 1 to 1 연결
    # on_delete ; 연결된 유저가 삭제될 때 연결된 profile도 같이 삭제됨
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    image = models.ImageField(upload_to='profile/', null=True)
    nickname = models.CharField(max_length=20, unique=True, null=True)
    message = models.CharField(max_length=100, null=True)