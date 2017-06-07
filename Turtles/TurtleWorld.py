import turtle
wn = turtle.Screen()
amit = turtle.Turtle()
amit.shape("turtle")
#amit.forward(50)
#amit.left(90)
#amit.forward(500)


l = 10
sides = 20
for i in range(0,sides):
    amit.forward(l)
    amit.right(65)
    amit.forward(l)
    amit.left(65*2)
    amit.forward(l)
    amit.right(65)
    amit.forward(l)
    amit.left(360/sides)

wn.mainloop()
