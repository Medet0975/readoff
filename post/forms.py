from django import forms
from post.models import Books

class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = "__all__"

        # def save(self, commit=True):
class SearchForm(forms.Form):
    query = forms.CharField()
