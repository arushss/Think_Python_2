def is_power(a,b):
    if a==b:
        return True
    elif (b==0) or (b==1) : # Exception cases
        return False
    if a%b==0 and is_power(a/b, b):
        return True
    
    return False

print(is_power(5,2))