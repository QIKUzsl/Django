from tinymce.models import HTMLField
from django.db import models
class Users(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    nickname = models.CharField(max_length=50, blank=True, null=True)
    age = models.IntegerField(default=18)
    email = models.EmailField(default="111@qq.com")
    password = models.CharField(max_length=255)

    header = models.CharField(max_length=255, verbose_name="头像")

    count = models.IntegerField(default=1)

    login_suo = models.DateTimeField(auto_now=True)


    gender_choices = (
        (0, "男"),
        (1, "女"),
    )
    gender = models.IntegerField(choices=gender_choices, default=1)

    # user = models.OneToOneField(on_delete=models.CASCADE)

