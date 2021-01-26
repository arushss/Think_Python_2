import math
def estimate_pi():
    counter=0
    term=0
    while term<pow(10,-15):
        term+=(math.factorial(4*counter)*(1103+26390*counter))/(pow(math.factorial(counter),4)*pow(396,4*counter))
        counter+=1
    answer=(2*math.sqrt(2)/9801)*term
    return answer

print("Rough estimate is ", estimate_pi())
print("Exact answer is ", 1/math.pi)