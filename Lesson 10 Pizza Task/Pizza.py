##"Задание: Система пиццерии"
#!Базовый класс Pizza содержит свойства: размер (small/medium/large), список ингредиентов (список строк), "
#!"цена (float). Добавьте метод calculate_price(), который считает стоимость на основе размера и ингредиентов (например, базовая цена + 1$ за каждый ингредиент).)"
#!Наследование: Классы MeatPizza (с мясными ингредиентами, переопределите calculate_price() с наценкой 20%) и VeggiePizza (овощная, скидка 10%)."
#!Инкапсуляция: Свойство _ingredients доступно только для чтения через геттер, метод add_ingredient() добавляет ингредиент с проверкой (не больше 10)."
#"Полиморфизм: Абстрактный базовый класс Order с методом prepare(), переопределенный для PizzaOrder (печатает рецепт и цену)."
# ?"Дополнительно: Класс Pizzeria с методом take_order(), который создает пиццу по выбору и выводит чек"

from abc import ABC, abstractmethod
# Базовый класс
class Pizza:
    def __init__(self, size, ingredients):
        self.size = size
        self._ingredients = ingredients  # Инкапсуляция
        self.price = 0.0

    def ingredients(self):
        return self._ingredients

    # Добавляем ингридиенты до 10 штук.
    def add_ingredient(self, item):
        if len(self._ingredients) < 10:
            self._ingredients.append(item)
        else:
            print("Слишком много ингредиентов!Можно не больше 10!")

    # Подсчет цены
    def calculate_price(self):

        if self.size == "large":
            base_price = 20.0
        elif self.size == "medium":
            base_price = 15.0
        else:
            base_price = 10.0
        # База + 1$ за каждый ингредиент
        total = base_price + len(self._ingredients)
        self.price = float(total)
        return base_price + len(self._ingredients)


# Наследники (Мясная и Овощная)
class MeatPizza(Pizza):
    def calculate_price(self):
        return super().calculate_price() * 1.2


class VeggiePizza(Pizza):
    def calculate_price(self):
        return super().calculate_price() * 0.9


# Абстрактный заказ (Полиморфизм)
class Order(ABC):
    @abstractmethod
    def prepare(self):
        pass


class PizzaOrder(Order):
    def __init__(self, pizza):
        self.pizza = pizza

    def prepare(self):
        price = int(self.pizza.calculate_price())

        if isinstance(self.pizza, MeatPizza):
            description = "мясную"
        elif isinstance(self.pizza, VeggiePizza):
            description = "овощную"
        else:
            description = "обычную"

        print(f"Готовим {description} пиццу {self.pizza.size}: цена {price}$")


# Запуск
my_pizza = MeatPizza("large", ["сыр", "грибы", "лук", "пепперони"])

# Создаем заказ
order = PizzaOrder(my_pizza)
order.prepare()

