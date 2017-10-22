from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):		#展示形式
	list_display = ('title', 'slug', 'author', 'publish', 'status')		
	list_filter = ('status', 'created', 'publish', 'author')	#侧边栏
	search_fields = ('title', 'body')	#搜索框
	prepopulited_fields = {'slug': ('title', )}
	raw_id_fields = ('author', )
	date_hierarchy = 'publish'
	odering = ['status', 'publish']

# Register your models here.
admin.site.register(Post, PostAdmin)
