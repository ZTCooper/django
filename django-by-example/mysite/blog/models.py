from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

# Create your models here.

class PublishedManager(models.Manager):
	def get_queryset(self):
		return super(PublishedManager, self).get_queryset().filter(status = 'published')

class Post(models.Model):
	STATUS_CHOICES = (
		('draft', 'Draft'),
		('published', 'Published'),
	)

	title = models.CharField(max_length = 250)
	slug = models.SlugField(max_length = 250, unique_for_date = 'publish')	#url短标签
	author = models.ForeignKey(User, related_name = 'blog_posts')	#多对一，一个用户可发多篇博客，关联User模型
	body = models.TextField()
	publish = models.DateTimeField(default = timezone.now)
	created = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now = True)
	status = models.CharField(max_length = 10,	choices = STATUS_CHOICES,	default = 'draft')
	objects = models.Manager()		#the default manager
	published = PublishedManager()		#our custom manager

	class Meta:
		ordering = ('-publish',)

	def __str__(self):
		return self.title

	def get_absolut_url(self):
		return reserve('blog:post_detail',
			args = [self.publish.year, publish.strftime('%m'), publish.strftime('%d'), self.slug]
			)

