# Generated by Django 4.1.13 on 2024-05-20 20:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="name",
            field=models.CharField(max_length=200, verbose_name="название"),
        ),
        migrations.AlterField(
            model_name="category",
            name="slug",
            field=models.SlugField(max_length=200, unique=True, verbose_name="слаг"),
        ),
        migrations.AlterField(
            model_name="product",
            name="available",
            field=models.BooleanField(default=True, verbose_name="доступен"),
        ),
        migrations.AlterField(
            model_name="product",
            name="category",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="products",
                to="shop.category",
                verbose_name="категория",
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="created",
            field=models.DateTimeField(auto_now_add=True, verbose_name="создан"),
        ),
        migrations.AlterField(
            model_name="product",
            name="description",
            field=models.TextField(blank=True, verbose_name="описание"),
        ),
        migrations.AlterField(
            model_name="product",
            name="image",
            field=models.ImageField(
                blank=True, upload_to="products/%Y/%m/%d", verbose_name="изображение"
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="name",
            field=models.CharField(max_length=200, verbose_name="название"),
        ),
        migrations.AlterField(
            model_name="product",
            name="price",
            field=models.DecimalField(
                decimal_places=2, max_digits=10, verbose_name="цена"
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="slug",
            field=models.SlugField(max_length=200, verbose_name="слаг"),
        ),
        migrations.AlterField(
            model_name="product",
            name="updated",
            field=models.DateTimeField(auto_now=True, verbose_name="обновлен"),
        ),
    ]
