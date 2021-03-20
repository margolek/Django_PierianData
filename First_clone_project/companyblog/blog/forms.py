from django import forms
from blog.models import Post,Comment

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ['author','title','text']

		#Add widgets which override default model option
		#https://docs.djangoproject.com/en/3.1/topics/forms/modelforms/#overriding-the-default-fields
		widgets = {
			#'class' refer to css class
			'title':forms.TextInput(attrs={'class':'textinputclass'}),
			'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea postconent'})
		}

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ['author','text']

		widgets = {
			'author':forms.TextInput(attrs={'class':'textinputclass'}),
			'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea'})
		}