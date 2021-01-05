import turtle
bob = turtle.Turtle()
def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)
    print(bob)
    turtle.mainloop()


square(bob, 250)