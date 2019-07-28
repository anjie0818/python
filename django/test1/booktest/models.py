from django.db import models

# Create your models here.
# 说明：不需要定义主键列，在生成时会自动添加，并且值为自动增长。
class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)
    bpub_date = models.DateField()
    bread = models.IntegerField(default=0)# 阅读量
    bcomment = models.IntegerField(default=0)# 评论数
    isDelete = models.BooleanField(default=False)#逻辑删除
class HeroInfo(models.Model):
    hname = models.CharField(max_length=20)
    hgender = models.BooleanField(default=True)
    isDelete = models.BooleanField(default=False)# 逻辑删除
    hcomment = models.CharField(max_length=100)# 英雄描述
    hbook = models.ForeignKey('BookInfo')# 英雄和图书的关系