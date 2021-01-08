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
    length=circum/50
    polygon(t,length,50)

def arc(t,r,angle):
    arc_length=r*2*math.pi*angle/360
    increment_length = arc_length / 50
    increment_angle = angle / 50
    
    for i in range(50):
        t.fd(increment_length)
        t.lt(increment_angle)
    turtle.mainloop()


arc(bob,70,180)
#circle(bob,100)
#square(bob, 250)