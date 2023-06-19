from django import forms
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

from .models import Post

class PostForm(ModelForm):

    class Meta:
        model = Post
        fields = '__all__'

        widgets ={
            'tags':forms.CheckboxSelectMultiple(),
        }


