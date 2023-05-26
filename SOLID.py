# Домашняя работа на 27.05.2023

# Модуль 14. Solid
# Тема: Solid

# Задание
# Создайте приложение для эмуляции работыпиццерии.
# Приложение должно иметь следующую функциональность:
# 1. Пользователь может выбрать из пяти стандартных
# рецептов пиццы или создать свой рецепт.
# 2. Пользователь может выбирать добавлять ли топпинги (сладкий лук, халапеньо, чили, соленный огурец,
# оливки, прошутто и т.д.).
# 3. Информацию о заказанной пицце нужно отображать
# на экран и сохранять в файл.
# 4. Расчет может производиться, как наличными, так и
# картой.
# 5. Необходимо иметь возможность просмотреть количество проданных пицц, выручку, прибыль.
# 6. Классы приложения должны быть построены с учетом принципов SOLID и паттернов проектирования


# Решение:
import json
# Класс для представления пиццы
class Pizza:
    def __init__(self, name, size, toppings, price):
        self.name = name  # Название пиццы
        self.size = size  # Размер пиццы (маленькая, средняя, большая)
        self.toppings = toppings  # Список топпингов
        self.price = price  # Цена пиццы

    def __str__(self):
        topp = ",".join(self.toppings)
        return f'{self.size} {self.name} pizza with {topp} for {self.price} rubles'

# Класс для создания пиццы
class PizzaBuilder:
    def __init__(self):
        self.name = ''
        self.size = ''
        self.toppings = []
        self.price = 0

    def set_name(self, name):
        self.name = name

    def set_size(self, size):
        self.size = size

    def add_topping(self, topping):
        self.toppings.append(topping)

    def calculate_price(self):
        # Расчёт цены пиццы
        if self.size == 'small':
            self.price = 500
        elif self.size == 'medium':
            self.price = 700
        elif self.size == 'large':
            self.price = 900
        for topping in self.toppings:
            if topping == 'sweet onion':
                self.price += 50
            elif topping == 'jalapeno':
                self.price += 70
            elif topping == 'chili':
                self.price += 80
            elif topping == 'pickle':
                self.price += 60
            elif topping == 'olives':
                self.price += 90
            elif topping == 'prosciutto':
                self.price += 120

    def build(self):
        # Создание объекта пиццы
        self.calculate_price()
        return Pizza(self.name, self.size, self.toppings, self.price)

# Класс для представления заказа
class Order:
    def __init__(self, pizza, quantity, payment_type):
        self.pizza = pizza  # Заказанная пицца
        self.quantity = quantity  # Количество заказанных пицц
        self.payment_type = payment_type  # Тип оплаты (наличные или карта)

    def calculate_total_price(self):
        # Расчёт стоимости заказа
        return self.pizza.price * self.quantity

# Класс для обработки заказов
class OrderController:
    def __init__(self):
        self.orders = [] # Список заказов

    def create_order(self, pizza, quantity, payment_type):
        # Создание заказа
        order = Order(pizza, quantity, payment_type)
        self.orders.append(order)
        return order

    def get_orders_count(self):
        # Получение количества проданных пицц
        return sum(order.quantity for order in self.orders)

    def get_total_revenue(self):
        # Получение выручки
        return sum(order.calculate_total_price() for order in self.orders)

    def get_profit(self):
        # Получение прибыли
        return self.get_total_revenue()*0.7  # Предполагаем, что прибыль составляет 70% от выручки

    def save_orders_to_file(self, filename):
        # Сохранение заказов в файл
        with open(filename, 'w') as f:
            json.dump([order.__dict__ for order in self.orders], f)

    def load_orders_from_file(self, filename):
        # Загрузка заказов из файла
        with open(filename, 'r') as f:
            orders_data = json.load(f)
            self.orders = [Order(**order_data) for order_data in orders_data]

pizza = PizzaBuilder()