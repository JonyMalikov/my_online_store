from django.db import models


class Category(models.Model):
    """Категория"""

    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ["name"]
        indexes = [
            models.Index(fields=["name"]),
        ]
        verbose_name = "категория"
        verbose_name_plural = "категории"

    def __str__(self):
        return self.name
