length = 50
size = 25
squarehit = 4
circlehit = 8
trihit = 3
evalnow = (squarehit > 0 and circlehit > 0 and trihit > 0)
import turtle
import time
import math
import random

def main():
  wn = turtle.Screen()
  wn.bgcolor('black')

  spaceship = turtle.Turtle()
  spaceship.color('gold','white')
  #spaceship.shape('turtle')
  #spaceship.resizemode("user")
  #spaceship.shapesize(10,10,20)
  #spaceship.shape('circle')
  #spaceship.shapesize(10,3)
  spaceship.penup()
  speed = 1 
  #spaceship.speed(100)

  def square(length):
    spaceship.pendown()
    spaceship.setheading(0)
    spaceship.fd(length)
    spaceship.lt(90)
    spaceship.fd(length)
    spaceship.lt(90)
    spaceship.fd(length)
    spaceship.lt(90)
    spaceship.fd(length)
    spaceship.lt(90)
    spaceship.penup()

  def triangle(length, angle):
    spaceship.pendown()
    spaceship.setheading(angle)
    spaceship.fd(length)
    spaceship.rt(120)
    spaceship.fd(length)
    spaceship.rt(120)
    spaceship.fd(length)
    spaceship.penup()

  spaceship.goto(200,0)
  square(length)
  spaceship.goto(-200,0)
  square(length)
  spaceship.goto(0,200)
  spaceship.pendown()
  spaceship.circle(size)
  spaceship.penup()
  spaceship.goto(0,0)

  def collision():
    if squarehit > 0:
        collision_square()
    if circlehit > 0:
      collision_circle()
    if trihit > 0:
      collision_triangle()

  def collision_square():
    if -200 <= int(spaceship.xcor()) <= -150 and 0 <= int(spaceship.ycor()) <= 50:
      squarehit = 0
      style = ('Courier', 30, 'Bold')
      spaceship.write('FIGHT!FIGHT!FIGHT!FIGHT!', font=style, align='center')
      print("squarehit", squarehit)

  def collision_circle():
    if math.sqrt(((int(spaceship.xcor()) - 0) ** 2) + (int(spaceship.ycor()) - 225) ** 2) <= 25:
      style = ('Courier', 30, 'Bold')
      spaceship.write('GAME OVER!', font = style, align = 'center')

  def collision_square2():
    if 200 <= int(spaceship.xcor()) <= 250 and 0 <= int(spaceship.ycor()) <= 50:
      style = ('Courier', 30, 'Bold')
      spaceship.write('HAHAHA!', font=style, align='center')

  def collision_laser():
    if squarehit > 0:
      lcollision_square()
    if circlehit > 0:
      lcollision_circle()
    if trihit > 0:
       lcollision_square2()

  def lcollision_square():
    if -200 <= int(spaceship.xcor()) <= -150 and 0 <= int(spaceship.ycor()) <= 50:
      global squarehit
      squarehit = squarehit - 1
      if squarehit <= 0:
        explosion1()


  def lcollision_circle():
    if math.sqrt(((int(spaceship.xcor()) - 0) ** 2) + (int(spaceship.ycor()) - 225) ** 2) <= 25:
      global circlehit
      circlehit = circlehit - 1
      if circlehit <= 0:
        explosion2()

  def lcollision_square2():
    if 200 <= int(spaceship.xcor()) <= 250 and 0 <= int(spaceship.ycor()) <= 50:
      global trihit
      trihit = trihit - 1
      if trihit <= 0:
        explosion3()

  def win_state():
    if trihit <= 0 and circlehit <= 0 and squarehit <= 0:
      style = ('Courier', 30, 'Bold')
      spaceship.write('BOOM!', font=style, align='center')
      global length
      length = 0

  def fup():
    spaceship.fd(5)
    collision()
    win_state()

  def fdn():
    spaceship.bk(5)
    collision()
    win_state()

  def flt():
    spaceship.lt(5)
    collision()
    win_state()

  def frt():
    spaceship.rt(5)
    collision()
    win_state()

  def laser():
    spaceship.speed(100000)
    spaceship.color('red','red')
    spaceship.pendown()
    spaceship.ht()
    spaceship.fd(100)
    collision_laser()
    spaceship.bk(100)
    spaceship.st()
    spaceship.speed(10000000)
    spaceship.color('black','black')
    spaceship.pendown()
    spaceship.ht()
    spaceship.fd(100)
    spaceship.bk(100)
    spaceship.st()
    spaceship.penup()
    spaceship.color('gold','white')
    spaceship.speed(100)
  
  def fire():
    laser()
    time.sleep(1)
    fire()
  
  def explosion1():
    del(fire)
    spaceship.goto(-200,50)
    spaceship.color('lightgrey','lightgrey')
    spaceship.setheading(90)
    spaceship.ht()
    spaceship.fd(75)
    spaceship.lt(90)
    spaceship.fd(25)
    spaceship.rt(45)
    spaceship.fd(25)
    spaceship.rt(45)
    spaceship.fd(25)
    spaceship.rt(45)
    spaceship.fd(25)
    spaceship.rt(45)
    spaceship.fd(100)
    spaceship.rt(45)
    spaceship.fd(25)
    spaceship.rt(45)
    spaceship.fd(25)
    spaceship.rt(45)
    spaceship.fd(25)
    spaceship.rt(45)
    spaceship.fd(25)
    spaceship.lt(90)
    spaceship.fd(75)
    spaceship.goto(-200,50)
    spaceship.color('black','black')
    spaceship.setheading(90)
    time.sleep(1.5)
    spaceship.fd(75)
    spaceship.lt(90)
    spaceship.fd(25)
    spaceship.rt(45)
    spaceship.fd(25)
    spaceship.rt(45)
    spaceship.fd(25)
    spaceship.rt(45)
    spaceship.fd(25)
    spaceship.rt(45)
    spaceship.fd(100)
    spaceship.rt(45)
    spaceship.fd(25)
    spaceship.rt(45)
    spaceship.fd(25)
    spaceship.rt(45)
    spaceship.fd(25)
    spaceship.rt(45)
    spaceship.fd(25)
    spaceship.lt(90)
    spaceship.fd(75)
    spaceship.goto(-200,0)
    spaceship.setheading(0)
    square(length)
    spaceship.goto(-200,50)
    spaceship.color('black','black')
    spaceship.setheading(90)
    spaceship.fd(75)
    spaceship.lt(90)
    spaceship.fd(25)
    spaceship.rt(45)
    spaceship.fd(25)
    spaceship.rt(45)
    spaceship.fd(25)
    spaceship.rt(45)
    spaceship.fd(25)
    spaceship.rt(45)
    spaceship.fd(100)
    spaceship.rt(45)
    spaceship.fd(25)
    spaceship.rt(45)
    spaceship.fd(25)
    spaceship.rt(45)
    spaceship.fd(25)
    spaceship.rt(45)
    spaceship.fd(25)
    spaceship.lt(90)
    spaceship.fd(75)
    spaceship.goto(-200,0)
    spaceship.setheading(0)
    square(length)
    del(collision_square)
    del(lcollision_square)
  
  def triangle_helix(angle):
    for x in range(100):
      triangle(length, angle)
      angle = angle + 7

  def explosion2():
    del(fire)
    spaceship.goto(0, 212.5)
    spaceship.color('red', 'red')
    triangle_helix(90)
    time.sleep(1.5)
    spaceship.color('black', 'black')
    spaceship.goto(0, 212.5)
    triangle_helix(90)
    spaceship.goto(0, 200)
    spaceship.setheading(0)
    spaceship.circle(size)
    del(collision_circle)
    del(lcollision_circle)

  def explosion3():
    del(fire)
    spaceship.goto(225, 25)
    spaceship.color('red', 'red')
    triangle_helix(90)
    time.sleep(1.5)
    spaceship.color('black', 'black')
    spaceship.goto(225, 25)
    triangle_helix(90)
    spaceship.goto(0, 200)
    spaceship.setheading(0)
    spaceship.circle(size)
    del(collision_square2)
    del(lcollision_square2)    

  wn.onkey(fup, "Up")
  wn.onkey(fdn, "Down")
  wn.onkey(flt, "Left")
  wn.onkey(frt, "Right")


  wn.listen()

  fire()

  if length == 0:
    exit()

main()
