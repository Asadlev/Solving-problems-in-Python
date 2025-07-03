"""
Python - Это 

Высокоуревнивый - Простой синтаксис, Легко читаемый и Близок к человеку

Интерпритируемый - Читает код с построчно, переводит написанный код -> в байт код а потом -> в Машинный код

Обьектно Ориентированный - Использование и Возможность писать ООП код

Динамическо Типизированный - Автоматическое распознование типа Обьекта

Общего назначение ЯП - Приеменение В люьых областях
"""


"""
1. Переменные
"""


"""
2. Типы данных
"""


"""
3. Условные операторы
"""


"""
4. Циклы
"""



"""
5. Функций
"""


"""
Задача 1
Есть список a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89].
Выведите все элементы, которые меньше 5.

Решение: 

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
result = [i for i in a if i < 5]
print(result)
"""

"""
Задача 2
Даны списки:
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89];
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

Нужно вывести числа общие для обейх списков

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

c = [i for i in a if i in b]
print(set(c))
"""




"""
Задача 3
Отсортируйте словарь 
по значению в порядке возрастания и убывания.

fruits = {
    "яблоко": 50,
    "апельсин": 20,
    "банан": 30,
    "груша": 10
}


fruits_list = list(fruits.items())

def get_price(fruit):
    return fruit[1]
sorted_list_p = sorted(fruits_list, key=get_price)
sorted_list_n = sorted(fruits_list, key=get_price, reverse=True)

sorted_fruits1 = dict(sorted_list_p)
sorted_fruits2 = dict(sorted_list_n)
print(sorted_fruits1)
print(sorted_fruits2)
"""



"""
Задача 4
Напишите программу для слияния нескольких словарей в один.

a = {
    "1": 1,
    "2": 2,
    "3": 3,
}
b = {
    "4": 4,
    "5": 5,
    "6": 6,
}

c = a | b
print(c)
"""




"""
Задача 5
Найдите три ключа с самыми высокими значениями в словаре
my_dict = {'a':500, 'b':5874, 'c':560, 'd':400, 'e':5874, 'f':20}

res = sorted(my_dict, key=my_dict.get, reverse=True)

print(res[:3])

"""



"""
Задача 6
Напишите код, который переводит целое число в строку, при том что его
можно применить в любой системе счисления.

def func(a=0, b=0):
    if type(a) == int:
        str_a = str(a)
        str_b = str(b)

    return str_a + str_b

print(func(5, 5))
"""



"""
Задача 7
Нужно вывести первые n строк треугольника Паскаля. В этом
треугольнике на вершине и по бокам стоят единицы, а каждое число
внутри равно сумме двух расположенных над ним чисел.

def pascal_triangle(n):
    triangle = []  # Список для хранения строк треугольника

    for i in range(n):
        # Создаем новую строку с единицами на краях
        row = [1] * (i + 1)

        # Заполняем внутренние значения строки (если строка длиннее двух элементов)
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

        # Добавляем строку в треугольник
        triangle.append(row)

    return triangle


# Вывод первых n строк треугольника Паскаля
n = int(input("Введите количество строк: "))
triangle = pascal_triangle(n)
for row in triangle:
    print(row)
"""




"""
-- ООП
"""


"""
Задача 1
Создайте класс "Человек" с атрибутами имя и возраст.
Добавьте метод, который возвращает строку с приветствием.

class Person:
    def __init__(self, first_name: str,  last_name : str, age:int):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def greet(self):
        return f"Привет, меня зовут {self.first_name} {self.last_name}, мне {self.age} лет."
"""


"""
Задача 3
Создайте классы "Автор" и "Книга". 
У каждой книги должен
быть автор. У книги также должны быть методы: "описание
книги" и "проверка принадлежности автору".

class Author:
    def __init__(self, first_name: str,  last_name : str):
        self.first_name = first_name
        self.last_name = last_name


class Book(Author):
    def __init__(self, first_name: str,  last_name : str, book: str):
        super().__init__(first_name,  last_name)
        self.book = book

    def greet(self):
        return f"Автором  {self.book} книги  является {self.first_name} {self.last_name}."


book1 = Book(
    'Лев',
    'Толстой',
    'Облачный Go'
)
result = book1.greet()
print(result)
"""



"""
Задача 4
Создайте класс "Сотрудник", 
от которого наследуются классы
"Менеджер" и "Разработчик". 
Переопределите метод
"работать" для каждой роли.

class Worker:
    def __init__(self, first_name: str,  salary: float):
        self.first_name = first_name
        self.salary= salary

    def work(self):
        return f" {self.first_name} работает в нашей компании"


class Manager(Worker):
    def __init__(self, first_name: str,  salary: float, position = str):
        super().__init__(first_name,salary)
        self.position = position

    def work(self):
        base_work = super().work()
        return f"{base_work} - Как {self.position} и получает зарплату ${self.salary} в год."


class Developer(Worker):
    def __init__(self, first_name: str, salary: float, position: str, language: str):
        super().__init__(first_name, salary)
        self.position = position
        self.language = language

    def work(self):
        base_work = super().work()
        return f"{base_work} -  Как {self.position} И Пишет код на {self.language} и получает зарплату ${self.salary} в год."

dev = Developer(
    'Иван',
    212,
    'Программист',
    'Python'
)
res = dev.work()
print(res)
"""




"""
Задача 5
Создайте класс "Банк", где каждый пользователь имеет
уникальный счёт. Реализуйте систему пополнения, снятия,
проверки баланса и ограничений на минимальный остаток.

class Bank:
    def __init__(self, name: str):  # исправлено __init__
        self.bank_name = name

    def greet(self):
        return f" Добро пожаловать в наш {self.bank_name}  банк"


class Client(Bank):
    def __init__(self, bank_name: str, client_first_name: str, amount: float, id: int):
        super().__init__(bank_name)
        self.client_first_name = client_first_name
        self._amount = amount
        self.id = id

    @property
    def clean_amount(self):
        return self._amount

    @clean_amount.setter
    def clean_amount(self, new_amount:int):
        if new_amount < 0:
            raise ValueError('Баланс не должен быть отрицательным')
        self._amount = new_amount
        return self._amount

    def greet(self):
        base_greet = super().greet()
        return f" {self.client_first_name} {base_greet} —  на вашем счету {self.id}  доступно {self._amount} "

client = Client(
    'Mbank',
    'Ivan',
    101,
    1
)
res = client.clean_amount = 1
print(res)
"""





"""
Задача 6
Создайте класс "Магазин", в котором хранятся товары и их
количество. Реализуйте методы: добавить товар, продать
товар, проверить наличие, вывести отчёт по складу.

class Shop:
    def __init__(self,name: str, products:list, quantity):
        self.name = name
        self.products = products
        self.quantity = quantity

    def add_product(self, add_product):
        self.add_product = add_product
        if self.quantity <= 0:
            return "Товар не был добавлен, так как он меньше нуля"
        self.quantity += 1
        self.products.append(add_product)
        
        return f"вы добавили {self.quantity} штук  в {self.product}"

    def sell(self, sell_product):
        for product in self.products:
            product = sell_product
            return f'Проданный товар: {product}'
        self.quantity -= 1
"""


