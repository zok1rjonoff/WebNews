from django.shortcuts import render

from newsInfo.models import NewsModel, CategoryModel


def all_news(request):
    news_list = NewsModel.objects.all().order_by('id').values()
    categories_list = CategoryModel.objects.all()
    return render(request, "index.html", {"news_list": news_list,"categories_list":categories_list})
