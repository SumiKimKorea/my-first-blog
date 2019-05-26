from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default = timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()
        
    def __str__(self):
        return self.title
    
"""
식별자 정리
_*  :다른 파일에서 접근 불가, 무시할때도 사용
__*__ : 시스템에서 정의한 이름. 
__*  : 클래스 안에서 외부로 노출되지 않는 식별자
"""