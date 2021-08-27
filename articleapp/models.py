from django.contrib.auth.models import User
from django.db import models


# Create your models here.
from projectapp.models import Project


class Article(models.Model):
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='article', null=True)
    #다중 연결을 해주어야한다. 다른 테이블과 연결 해준다. 작성자 미상의 글로 남도록 해준다.
    #누군가 탈퇴를 한 상황에
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, related_name='article', null=True)
    title = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to="article/", null=True)
    # 관련한 이미지가 쌀인다.
    content = models.TextField(null=True)
    #장문이 될수 있는 경우 사용한다.

    created_at = models.DateField(auto_now_add=True, null=True)

    like = models.IntegerField(default=0)