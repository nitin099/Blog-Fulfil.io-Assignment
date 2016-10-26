from django.contrib import admin
from .models import Post
# Register your models here.


class PostAdmin(admin.ModelAdmin):
	list_display = ['user',"title" , 'content' , 'publish' , 'draft' , 'timestamp','update','id']
	class Meta:
		model = Post


admin.site.register(Post ,PostAdmin)