# =========================
# 用 python manage.py makemigrations 建立migration
# 用 python manage.py migrate 正式建立資料表到資料庫
# 用 python manage.py shell 可以在終端機中建立python程式環境
# 用 資料表.objects.get(篩選條件) 取得目標資料
# =========================
from django.db import models
from django.utils import timezone  # for django to get time
from django.contrib.auth.models import User # 取用auth_user資料表資料


# Create your models here.
# =========================
# timezone.now不需要括號
# models.CASCADE不會在刪除post時刪除user，但刪除user會同時刪除post
# =========================
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    # timezone.now不需要括號()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
