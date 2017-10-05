from django.http import HttpResponse
from django.shortcuts import render_to_response
from blog.models import BlogPost

# Create your views here.
def archives(request):
	posts = BlogPost.objects.all()		#获取database中所拥有BlogPost对象
	return render_to_response('archive.html',{'posts': posts})