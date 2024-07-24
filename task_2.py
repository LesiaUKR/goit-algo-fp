import turtle
import math

def draw_pythagoras_tree(order, size, angle=45):
    if order == 0:
        turtle.forward(size)
        turtle.backward(size)
    else:
        turtle.pensize(2) 
        turtle.pencolor("blue")
        turtle.fillcolor("green")
        turtle.begin_fill()
        turtle.forward(size)
        turtle.left(angle)
        draw_pythagoras_tree(order - 1, size * math.cos(math.radians(angle)), angle)
        turtle.right(2 * angle)
        draw_pythagoras_tree(order - 1, size * math.cos(math.radians(angle)), angle)
        turtle.left(angle)
        turtle.backward(size)

if __name__ == "__main__":
   # Ініціалізація turtle
   turtle.speed(0)
   turtle.left(90)

   screen = turtle.Screen()
   screen.title("Дерево Піфагора")

   # Отримання рівня рекурсії від користувача
   level = int(input("Введіть рівень рекурсії (ціле число): "))
   size = 100

   # Малювання дерева Піфагора
   draw_pythagoras_tree(level, size)

   # Завершення роботи turtle
   turtle.done()