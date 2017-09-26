from django.contrib import admin
from books.models import Publishier, Author,Book

class AuthorAdmin(admin.ModelAdmin):
	#从django.contrib.admin.ModelAdmin派生出来的子类
	list_display = ('first_name', 'last_name', 'email')
	search_fields = ('first_name', 'last_name')

class BookAdmin(admin.ModelAdmin):
	list_display = ('title', 'publishier', 'publication_date')
	list_filter = ('publication_date',)
	date_hierarchy = 'publication_date'		#两种日期过滤
	ordering = ('-publication_date',)		#排序
	fileds = ('title', 'author', 'publishier', 'publication_date')
	#编辑表单
	#fileds = ('title', 'author', 'publishier',)
	#可隐藏'publication_date'防止被编辑
	filter_horizontal = ('authors',)	#manytomany
	raw_id_fields = ('publishier',)		#foreinkey

# Register your models here.
admin.site.register(Publishier)
admin.site.register(Author, AuthorAdmin)	
#用AuthorAdmin选项注册Author模块
#如果忽略第二个参数，Django将使用默认选项
admin.site.register(Book, BookAdmin)