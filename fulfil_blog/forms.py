from django import forms
from .models import Post

from pagedown.widgets import PagedownWidget

class PostForm(forms.ModelForm):
	content		 = forms.CharField(widget = PagedownWidget)
	publish		 = forms.DateTimeField(widget = forms.SelectDateWidget)

	class Meta:
		model = Post
		fields = [
		"title",
		"image",
		"content",
		"draft",
		"publish"
		]
