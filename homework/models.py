class Product:
    """
    Класс продукта
    """
    name: str
    price: float
    description: str
    quantity: int

    def __init__(self, name, price, description, quantity):  # вызывается при создании класса и
        # инициализирует его атрибуты
        self.name = name
        self.price = price
        self.description = description
        self.quantity = quantity

    def check_quantity(self, quantity) -> bool:  # self - сcылка на текущий объект.
        # Метод объекта, который сравнивает кол-во продуктов
        """
        TODO Верните True если количество продукта больше или равно запрашиваемому
            и False в обратном случае
        """
        if self.quantity >= quantity:
            return True
        else:
            return False

    def buy(self, quantity):  # self - сылка на текущий объект.
        # Метод объекта, который покупает
        """
        TODO реализуйте метод покупки
            Проверьте количество продукта используя метод check_quantity
            Если продуктов не хватает, то выбросите исключение ValueError
        """
        if self.check_quantity(quantity):
            self.quantity -= quantity
        else:
            raise ValueError("Продуктов не хватает!")

    def __hash__(self):  # нужен для быстрого сравнения объектов.
        # Метод должен возвращать целочисленное значение,
        # которое будет использоваться для быстрого сравнения ключей в словарях
        return hash(self.name + self.description)


class Cart:
    """
    Класс корзины. В нем хранятся продукты, которые пользователь хочет купить.
    TODO реализуйте все методы класса
    """

    # Словарь продуктов и их количество в корзине
    products: dict[Product, int]

    def __init__(self):
        # По-умолчанию корзина пустая
        self.products = {}

    def add_product(self, product: Product, buy_count=1):
        """
        Метод добавления продукта в корзину.
        Если продукт уже есть в корзине, то увеличиваем количество
        """
        if product in self.products:  # проверяем наличие продукта
            self.products[product] += buy_count
        else:
            self.products[product] = buy_count

    def remove_product(self, product: Product, remove_count=None):
        """
        Метод удаления продукта из корзины.
        Если remove_count не передан, то удаляется вся позиция
        Если remove_count больше, чем количество продуктов в позиции, то удаляется вся позиция
        """
        if product in self.products:  # проверяем наличие продукта
            if remove_count is None or remove_count >= self.products[product]:  # сравниваем
                del self.products[product]  # удаляем
            elif remove_count < self.products[product]:
                self.products[product] -= remove_count

    def clear(self):
        # Метод очистки корзины
        self.products.clear()  # почистили корзину

    def get_total_price(self) -> float:
        # Метод нахождения общей стоимости товаров в корзине
        total = 0  # начальная общая
        for product, count in self.products.items():  # перебираем продукты
            total += product.price * count
        return total  # итоговая общая

    def buy(self):
        """
        Метод покупки.
        Учтите, что товаров может не хватать на складе.
        В этом случае нужно выбросить исключение ValueError
        """
        for product, store in self.products.items():
            if product.quantity < store:
                raise ValueError("Продуктов не хватает!")
            else:
                product.buy(store)
