from django import forms

from newsInfo.models import NewsModel


class SearchForms(forms.Form):
    search_bar = forms.CharField(max_length=256)


class UploadImage(forms.ModelForm):
    class Meta:
        model = NewsModel
        fields = ('news_title', 'news_description', 'news_image')