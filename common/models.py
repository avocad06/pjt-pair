from django.db import models

# Create your models here.

class Common(models.Model):
    name = models.CharField(max_length=64, verbose_name = '사용자 이름')
    password = models.CharField(max_length=64, verbose_name = '비밀번호')
    registered_dttm = models.DateTimeField(auto_now_add=True, verbose_name='등록 시간')
    
    def __str__(self):
        return self.username

    class Meta:
        db_table = 'test_user'
        