def power(x,n):
    ans=1
    if n==0:
        return ans
    for i in range(n):
        ans=ans*x
    return ans

def check_fermat(a,b,c,n):
    if n>2 and (power(a,n)+power(b,n)==power(c,n)):
        print("Holy Smokes, Fermat was wrong!\n")
    else:
        print("No, that doesn't work\n")

print("Enter four numbers one after other\n")
a=eval(input())
b=eval(input())
c=eval(input())
n=eval(input())

check_fermat(a,b,c,n)
