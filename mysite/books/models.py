from django.db import models

# Create your models here.
# 每个数据模型都是django.db.models.Model的子类

class Publishier(models.Model):     #所有模型自动拥有objects管理器，查找数据时使用
    name = models.CharField(max_length = 30)
    address = models.CharField(max_length = 50)
    city = models.CharField(max_length = 60)
    state_province = models.CharField(max_length = 30)
    country = models.CharField(max_length = 50)
    website = models.URLField()

    def __str__(self):
        return self.name 

    #class Meta:
    #   ordering = ['name']

class Author(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 40)
    email = models.EmailField(blank = True, verbose_name = 'e-mail')     #该字段可选

    def __str__(self):
        return u'%s %s' % (self.first_name, self.last_name)

class Book(models.Model):
    title = models.CharField(max_length = 100)
    authors = models.ManyToManyField(Author)        #多对多
    publishier = models.ForeignKey(Publishier)      #一对多
    publication_date = models.DateField(blank = True, null = True)  #允许字段为空

    def __str__(self):
        return self.title
