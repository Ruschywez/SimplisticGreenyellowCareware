import random


class Item:
    def __init__(self, name):
        self.name = name
        self.__value = 0

    # Возвращает значение предмета для использования
    def use(self):
        return self.__value

# Продолжи писать решение тут
class Food(Item):
    def __init__(self, name):
        super().__init__(name)
        self.name = name
        self.__value = random.randint(1, 10)


# Объекты от этого класса тут создавать не нужно, сделай это у себя.
cake = Food("cake")
print(cake.use())