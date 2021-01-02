# Program that prints a grid
def print1():
    print('+', '- - - -', '+', '- - - -', '+')

def print2():
    print('|', '       ', '|', '       ', '|')

def grid():
    print1()
    for x in range(4):
        print2()
    print1()
    for x in range(4):
        print2()
    print1()

grid()