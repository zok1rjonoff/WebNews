from django.db import models


class CategoryModel(models.Model):
    category_title = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    # Instead of showing category model added it is better to display category name
    def __str__(self):
        return self.category_title

    class Meta:
        # strictly in order
        verbose_name = "News category",
        verbose_name_plural = "News categories"


class NewsModel(models.Model):
    news_title = models.TextField(help_text="Название товара")
    news_category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, null=True, blank=True)
    news_description = models.TextField()
    news_image = models.FileField(upload_to="news_images")
    news_created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.news_title

    class Meta:
        # strictly in order
        verbose_name = "News"
        verbose_name_plural = "News info"
