"""
Протестируйте классы из модуля homework/models.py
"""
import pytest

from homework.models import Product, Cart


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)


@pytest.fixture
def cart():
    return Cart()


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):
        # TODO напишите проверки на метод check_quantity
        assert product.check_quantity(10)
        assert product.check_quantity(1001) == False
        assert product.check_quantity(999)

    def test_product_buy(self, product):
        # TODO напишите проверки на метод buy
        product.buy(10)
        assert product.check_quantity(666)

    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        with pytest.raises(ValueError):
            product.buy(1002)


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """

    def test_product_add_product(self, product, cart):
        cart.add_product(product, 5)
        assert cart.products[product] == 5

    def test_product_remove_product(self, product, cart):
        cart.add_product(product, 2)
        cart.remove_product(product, 1)
        assert cart.products[product] == 1

    def test_product_clear(self, product, cart):
        cart.add_product(product, 6)
        cart.clear()

    def test_product_get_total_price(self, product, cart):
        cart.add_product(product, 6)
        assert cart.get_total_price() == 600

    def test_product_get_total_price(self, product, cart):
        assert cart.get_total_price() == 0

    def test_product_buy(self, product, cart):
        product.quantity = 1000
        cart.add_product(product, 1002)
        with pytest.raises(ValueError):
            cart.buy()
