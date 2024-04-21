# Автор Ігор Хруневич Igor_lv@ex.ua 
# Цю міні-програму створено, щоб зацікавити дітей програмуванням
# Користуйтесь, вивчайте, досліджуйте, змінюйте - експериментуйте

from math import sqrt
import turtle
import random
import math

print("Розрахуйте S площу трикутника ")
print("Введіть розміри трикутника:")
a = float(input("Введіть розмір основи трикутника ? = "))
b = float(input("Введіть розмір сторони ? = "))
c = float(input("Введіть розмір другої сторони ? = "))
p = (a + b + c) / 2
s = (p*(p-a)*(p-b)*(p-c)) ** 0.5 
print("Площа: %0.2f" %s)
print ("Поки Ви звіряєте свій розв'язок із розв'язком даної програми, черепашка намалювала Вам ваш трикутник. Знайдіть його у себе на моніторі.")
# set turtle
window = turtle.Screen()
writer = turtle.Turtle()
writer.pensize(3)
writer.pencolor("black")
writer.pendown

def checkTriangle():
  side1 = (a*37)
  side2 = (b*37)
  side3 = (c*37)

  sum1and2 = side1 + side2
  sum1and3 = side1 + side3
  sum2and3 = side2 + side3


  angle1 = angle(side1, side2, side3)
  angle2 = angle(side2, side3, side1)
  angle3 = angle(side3, side1, side2)
  
  


  if side3 <= sum1and2 and side2 <= sum1and3 and side1 <= sum2and3:
    print ("true")
    print(side1, side2, side3)
    print(angle1, angle2, angle3)
    drawTriangle(side1, side2, side3, angle1, angle2, angle3)
    
  else:
    print ("false")

def angle(side1, side2, side3):
  return math.degrees(math.acos((side3**2 - side2**2 - side1**2) /(2.0 * side1 * side2)))

def drawTriangle(side1, side2, side3, angle1, angle2, angle3):
  writer.forward(side1)
  writer.left(angle1)
  writer.forward(side2)
  writer.left(angle2)
  writer.forward(side3)
  writer.left(angle3)
  writer.hideturtle()
  
checkTriangle()
style = ('Courier', 15, 'italic')
turtle.write(" Turtle накреслила\n Вам ваш трикутник", font=style, align='right')
turtle.title('Ваш трикутник')  
