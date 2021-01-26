def eval_loop():
    counter=0
    while True:
        print("input something")
        a=eval(input())
        if a!='done':
            c=a
            print(a)
        else :
            if counter>0:
                print(c)
            break
        counter+=1

eval_loop()
