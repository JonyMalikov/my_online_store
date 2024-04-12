from django.db import models
from django.urls import reverse


class Category(models.Model):
    """Категория"""

    name = models.CharField(max_length=200, verbose_name="название")
    slug = models.SlugField(max_length=200, unique=True, verbose_name="слаг")

    class Meta:
        ordering = ["name"]
        indexes = [
            models.Index(fields=["name"]),
        ]
        verbose_name = "категория"
        verbose_name_plural = "категории"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """Абсолютная ссылка на категорию"""
        return reverse("shop:product_list_by_category", args=[self.slug])


class Product(models.Model):
    """Продукт"""

    category = models.ForeignKey(
        Category,
        related_name="products",
        on_delete=models.CASCADE,
        verbose_name="категория",
    )
    name = models.CharField(max_length=200, verbose_name="название")
    slug = models.SlugField(max_length=200, verbose_name="слаг")
    image = models.ImageField(
        blank=True, upload_to="products/%Y/%m/%d", verbose_name="изображение"
    )
    description = models.TextField(blank=True, verbose_name="описание")
    price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="цена"
    )
    available = models.BooleanField(default=True, verbose_name="доступен")
    created = models.DateTimeField(auto_now_add=True, verbose_name="создан")
    updated = models.DateTimeField(auto_now=True, verbose_name="обновлен")

    class Meta:
        ordering = ["name"]
        indexes = [
            models.Index(fields=["id", "slug"]),
            models.Index(fields=["name"]),
            models.Index(fields=["-created"]),
        ]
        verbose_name = "продукт"
        verbose_name_plural = "продукты"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """Абсолютная ссылка на продукт"""
        return reverse("shop:product_detail", args=[self.id, self.slug])
