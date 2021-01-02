# Program that prints a grid
def print1():
    print('+', 4 * '-', '+', 4 * '-', '+')

def print2():
    print('|', 4 * ' ', '|', 4 * ' ', '|')

def grid():
    print1()
    for x in range(4):
        print2()
    print1()
    for x in range(4):
        print2()
    print1()

grid()