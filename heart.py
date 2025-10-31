import turtle
import math

# Настройка окна
t = turtle.Turtle()
t.speed(0)  
t.color("red")  
turtle.bgcolor("black")  
# Функция для расчета координат сердца
def corazon(n):
    x = 16 * math.sin(n) ** 3
    y = 13 * math.cos(n) - 5 * math.cos(2 * n) - 2 * math.cos(3 * n) - math.cos(4 * n)
    return x, y

# Рисуем сердца
t.penup()
for i in range(1, 17): 
    t.goto(0, 0)  
    t.pendown()
    for n in range(0, 360, 3):  
        x, y = corazon(math.radians(n))  
        t.goto(x * i, y * i)  
    t.penup()

t.hideturtle()  

turtle.done() 
