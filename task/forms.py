from django import forms
from .models import Article,Img


class ArticleForm(forms.ModelForm):
	class Meta:
		model=Article
		fields=('author','title','body')

class ImgForm(forms.ModelForm):
	class Meta:
		model=Img
		fields=('image',)
   


