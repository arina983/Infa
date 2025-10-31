import turtle
import math

# Настройка окна
t = turtle.Turtle()
t.speed(0)  # Устанавливаем максимальную скорость
t.color("red")  # Цвет линии
turtle.bgcolor("black")  # Цвет фона

# Функция для расчета координат сердца
def corazon(n):
    x = 16 * math.sin(n) ** 3
    y = 13 * math.cos(n) - 5 * math.cos(2 * n) - 2 * math.cos(3 * n) - math.cos(4 * n)
    return x, y

# Рисуем сердца
t.penup()
for i in range(1, 17):  # Увеличиваем размер сердца
    t.goto(0, 0)  # Перемещаем черепашку в центр
    t.pendown()
    for n in range(0, 360, 3):  # Угол от 0 до 360 градусов
        x, y = corazon(math.radians(n))  # Преобразуем градусы в радианы
        t.goto(x * i, y * i)  # Увеличиваем размер сердца
    t.penup()

t.hideturtle()  # Скрываем черепашку
turtle.done()  # Завершаем работу