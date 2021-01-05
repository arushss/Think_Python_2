import turtle
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

polygon(bob,200,4)
#square(bob, 250)