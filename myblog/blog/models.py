from django.db import models

# Create your models here.
#定义blog数据结构

class BlogPost(models.Model):
	title = models.CharField(max_length = 150)	#博客标题
	body = models.TextField()	#博客正文
	timestamp = models.DateTimeField()	#博客创建时间

