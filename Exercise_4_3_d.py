import turtle
import math
bob = turtle.Turtle()
def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)
    print(bob)
    turtle.mainloop()

def polygon(t, length, n):
    for i in range(n):
        t.fd(length)
        t.lt(360/n)
    print(bob)
    turtle.mainloop()

def circle(t, r):
    circum=2*math.pi*r
    length=circum/200
    polygon(t,length,200)


circle(bob,50)
#square(bob, 250)