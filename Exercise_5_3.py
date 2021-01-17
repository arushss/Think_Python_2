def is_triangle(a,b,c):
    if a>b+c or b>a+c or c>a+b:
        print("No")
    else:
        print("Yes")

print("Enter three sides of a triangle one after other\n")
a=eval(input())
b=eval(input())
c=eval(input())

is_triangle(a,b,c)