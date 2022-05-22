from django.db import models

# 블로그는 다양한 포스트 단위로 구분
# 하나의 포스트에는 제목, 내용, 작성시간 정보가 들어있을 예정

# django.db.models.Model 을 상속 받는 클래스를 정의하게 되면 
# django가  관리하는 하나의 데이터 모델이 생성되는 것
class Post(models.Model) : 

    title = models.CharField(max_length=200)
    content = models.CharField(max_length=2048)
    #제목과 내용은 문자열로 된 필드,
    date = models.DateTimeField(auto_created=True, auto_now=True)
    #  작성 시간은 ‘자동으로 생성
    # 현재 시간이 자동으로 기록되는’ DateTime 필드