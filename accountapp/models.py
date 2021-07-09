from django.db import models

# Create your models here.
#모델하나를 적는데 이것이 데이터베이스의 데이블 같은것이 된다.
#상속을 받는다,
#장고에서 기본으로 제공해주는 기초 모델
class NewModel(models.Model):
    text = models.CharField(max_length=225, null=False)

#문자열을 입력받는 모델