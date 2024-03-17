from django.contrib import admin

from newsInfo.models import CategoryModel, NewsModel


@admin.register(CategoryModel)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["pk", "category_title", "created_at"]
    search_fields = ['category_title', "pk"]
    list_filter = ["created_at"]
    ordering = ["-created_at"]


@admin.register(NewsModel)
class NewsModelAdmin(admin.ModelAdmin):
    list_display = ["pk", 'news_title', "news_category", "news_description", "news_image", "news_created_at"]
    search_fields = ['news_title', "pk"]
    list_filter = ["news_created_at"]
    ordering = ["-news_created_at"]
