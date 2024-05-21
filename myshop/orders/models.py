from django.db import models
from shop.models import Product


class Order(models.Model):
    """Заказ"""

    first_name = models.CharField(max_length=50, verbose_name="имя")
    last_name = models.CharField(max_length=50, verbose_name="фамилия")
    email = models.EmailField(verbose_name="электронная почта")
    address = models.CharField(max_length=250, verbose_name="адрес")
    postal_code = models.CharField(
        max_length=20, verbose_name="почтовый индекс"
    )
    city = models.CharField(max_length=100, verbose_name="город")
    created = models.DateTimeField(auto_now_add=True, verbose_name="создан")
    updated = models.DateTimeField(auto_now=True, verbose_name="обновлен")
    paid = models.BooleanField(default=False, verbose_name="оплачен")

    class Meta:
        ordering = ["-created"]
        verbose_name = "заказ"
        verbose_name_plural = "заказы"
        indexes = [
            models.Index(fields=["-created"]),
        ]

    def __str__(self):
        return f"Order {self.id}"

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    """Позиция в заказе"""

    order = models.ForeignKey(
        Order,
        related_name="items",
        on_delete=models.CASCADE,
        verbose_name="заказ",
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="order_items",
        verbose_name="продукт",
    )
    price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="цена"
    )
    quantity = models.PositiveIntegerField(
        default=1, verbose_name="количество"
    )

    def __str__(self):
        return str(self.id)

    def get_cost(self):
        return self.price * self.quantity
