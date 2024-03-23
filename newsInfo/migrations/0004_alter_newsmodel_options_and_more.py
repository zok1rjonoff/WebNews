# Generated by Django 5.0.3 on 2024-03-21 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsInfo', '0003_alter_newsmodel_news_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='newsmodel',
            options={'verbose_name': 'News', 'verbose_name_plural': 'News info'},
        ),
        migrations.AlterField(
            model_name='categorymodel',
            name='category_title',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='newsmodel',
            name='news_title',
            field=models.TextField(help_text='Название товара'),
        ),
    ]
