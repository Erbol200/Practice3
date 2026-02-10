# базовый класс
class Shape:
    def area(self):
        return 0

# класс Rectangle наследует Shape
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# ввод данных
length, width = map(int, input().split())

# создаём объект и выводим площадь
rect = Rectangle(length, width)
print(rect.area())
