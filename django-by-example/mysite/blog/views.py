from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post

# Create your views here.

def post_list(request):
	posts = Post.published.all()
	object_list = Post.published.all()
	paginator = Paginator(object_list, 3)	#每页3个post
	page = request.GET.get('page')
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:		#不是整数
		posts = paginator.page(1)	#返回第一页
	except EmptyPage:	#超出最大
		posts = paginator.page(paginator.num_pages)		#返回最后一页
	return render(request, 'blog/post/list.html', {'page':page, 'posts': posts})

def post_detail(request, year, month, day, post):
	post = get_bject_or_404(Post,
		slug = post,
		status = 'published',
		publish_year = year,
		publish_month = month,
		publish_day = day,
		)
	return render(request, 'blog/post/detail.html', {'posts': posts})
