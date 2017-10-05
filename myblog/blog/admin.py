from django.contrib import admin
from blog.models import BlogPost

class BlogPostAdmin(admin.ModelAdmin):
	list_display = ('title', 'timestamp')

# Register your models here.
admin.site.register(BlogPost, BlogPostAdmin)