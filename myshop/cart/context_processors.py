from .cart import Cart


def cart(request):
    """подробная информация о корзине"""
    return {"cart": Cart(request)}
