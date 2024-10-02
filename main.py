import turtle

turtle.setup(1000,1000,0,0)

a=turtle.Turtle()
a.width(8)
a.color("red")
new=turtle.getscreen()
a.speed(4)

new.bgcolor("lightblue")

# Hidden Work(penup)
a.left(180)
a.penup()
a.forward(300)
a.right(90)
a.forward(100)
a.pendown()

# Printing H


#start to draw
a.forward(50)
a.right(90)
a.forward(50)
a.left(90)
a.forward(50)
a.left(90)

a.penup()
a.forward(50)
a.left(90)
a.pendown()
a.forward(50)
a.left(90)
a.forward(50)
a.right(90)
a.forward(50)


# printing A

a.penup()
a.left(90)
a.forward(15)
a.pendown()
a.left(70)
a.forward(110)
a.right(70)
a.right(70)
a.forward(110)
a.left(180)
a.forward(55)
a.left(70)
a.forward(38)
a.left(70)
a.penup()
a.forward(55)
a.left(110)

a.forward(100)

# printing P

a.left(90)
a.pendown()
a.forward(100)
a.right(90)
a.forward(50)
a.right(20)
a.forward(20)
a.right(70)
a.forward(40)
a.right(70)
a.forward(20)
a.right(20)
a.forward(50)
a.left(90)
a.forward(50)
a.left(90)
a.penup()
a.forward(100)


# printing P

a.left(90)
a.pendown()
a.forward(100)
a.right(90)
a.forward(50)
a.right(20)
a.forward(20)
a.right(70)
a.forward(40)
a.right(70)
a.forward(20)
a.right(20)
a.forward(50)
a.left(90)
a.forward(50)
a.left(90)
a.penup()
a.forward(100)

# printing Y

a.forward(20)
a.pendown()
a.left(90)
a.forward(50)
a.left(30)
a.forward(60)
a.backward(60)
a.right(60)
a.forward(60)
a.backward(60)
a.left(30)

# go to Home

a.penup()
a.home()

a.color("orange")
new.bgcolor("lightgreen")
# setting second row

a.backward(300)
a.right(90)
a.forward(60)
a.left(180)


# printing B


a.pendown()
a.forward(100)
a.right(160)
a.forward(100)
a.left(160)
a.forward(100)



# go to Home

a.penup()
a.home()

# setting up

a.backward(240)
a.right(90)
a.forward(10)
a.pendown()
a.forward(50)
a.left(90)
a.forward(50)
a.backward(50)
a.left(90)
a.forward(100)
a.right(90)
a.forward(50)
a.backward(50)
a.right(90)
a.forward(50)
a.left(90)
a.forward(50)
a.penup()
a.home()

# set up for W

a.backward(150)
a.right(90)
a.forward(60)
a.pendown()
a.backward(100)
a.forward(100)
a.left(120)
a.forward(40)
a.right(60)
a.forward(40)
a.left(120)
a.forward(100)
a.penup()
a.home()

# set up for Y

a.backward(30)
a.right(90)
a.forward(65)
a.left(90)



# set up for Y


a.pendown()
a.left(90)
a.forward(50)
a.left(30)
a.forward(60)
a.backward(60)
a.right(60)
a.forward(60)
a.backward(60)
a.left(30)

# go to Home 

a.penup()
a.home()


# printing E

a.forward(10)
a.right(90)
a.forward(10)
a.pendown()
a.forward(50)
a.left(90)
a.forward(50)
a.backward(50)
a.left(90)
a.forward(100)
a.right(90)
a.forward(50)
a.backward(50)
a.right(90)
a.forward(50)
a.left(90)
a.forward(50)
a.penup()
a.home()


# set up for A
a.forward(90)

# printing A

a.right(90)
a.forward(50)
a.left(90)
a.pendown()
a.left(70)
a.forward(110)
a.right(70)
a.right(70)
a.forward(110)
a.left(180)
a.forward(55)
a.left(70)
a.forward(38)
a.left(70)
a.penup()
a.forward(55)
a.left(110)

a.forward(100)


#go to home
a.penup()
a.home()


# set up for R
a.forward(180)
a.right(90)
a.forward(50)
a.left(180)

#set up for R
a.pendown()
a.forward(100)
a.right(90)
a.forward(50)
a.right(20)
a.forward(20)
a.right(70)
a.forward(40)
a.right(70)
a.forward(20)
a.right(20)
a.forward(50)
a.left(180)
a.forward(50)
a.right(20)
a.forward(20)
a.right(70)
a.forward(40)
a.left(180)
a.penup()
a.home()

# setting position

a.right(90)
a.forward(215)
a.right(90)
a.forward(170)


#color

a.color("green")
new.bgcolor("lightblue")





#design pattern
a.home()
a.forward(370)
a.pendown()
a.color("hotpink")
a.width(3)
a.speed(0)

def squre(length, angle):
    
    a.forward(length)
    a.right(angle)
    a.forward(length)
    a.right(angle)
   
    a.forward(length)
    a.right(angle)
    a.forward(length)
    a.right(angle)

squre(80, 90)

for i in range(36):
      a.right(10)
      squre(80, 90)



a.penup()
a.home()
a.left(90)
a.forward(270)
a.left(90)
a.forward(200)
a.pendown()

def draw_star(size, color):
    angle = 120
    a.fillcolor(color)
    a.begin_fill()

    for side in range(5):
        a.forward(size)
        a.right(angle)
        a.forward(size)
        a.right(72 - angle)
    a.end_fill()
    return

draw_star(30, "purple")



turtle.mainloop()