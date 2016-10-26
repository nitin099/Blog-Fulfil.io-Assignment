from django.db import models
from django.conf import settings
from markdown_deux import markdown
from django.utils.safestring import mark_safe
from django.contrib.contenttypes.models import ContentType
from comments.models import Comments
from django.core.urlresolvers import reverse

# Create your models here.
class Post(models.Model):
	user 		= models.ForeignKey(settings.AUTH_USER_MODEL,default = 1)
	title 		= models.CharField(max_length=20)
	image		= models.ImageField(null = True,
					blank= True,
					width_field = "width_field",
					height_field = 'height_field')
	height_field= models.IntegerField(default=0)
	width_field = models.IntegerField(default=0)
	content 	= models.TextField()
	draft 	 	= models.BooleanField(default=False)
	publish		= models.DateTimeField(auto_now = False,auto_now_add = False)
	update		= models.DateTimeField(auto_now = True ,auto_now_add = False)
	timestamp 	= models.DateTimeField(auto_now_add = True , auto_now = False)

	class Meta:
		ordering = ['-update','-timestamp'  ]
	
	def get_markdown(self):
		content = self.content
		return mark_safe(markdown(content))

	@property
	def comments(self):
		instance = self
		qs  = Comments.objects.filter_by_instance(instance)
		return qs
	
	@property
	def get_content_type(self):
		instance = self
		content_type  = ContentType.objects.get_for_model(instance.__class__)
		return content_type


	def get_absolute_url(self):
		return reverse("detail" , kwargs ={"id" : self.id})