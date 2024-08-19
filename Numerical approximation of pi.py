#Numerical approximation of pi
import math

def fact(x):
    if x == 0:
        return 1
    else:
        return x* fact(x-1)
result = 0
k = 0

while True:
    
    term =((fact(4*k)*(1103 + 26390*k))/((fact(k)**4)*(396)**(4*k)))
    result += term
    if abs(term) < 1e-15:
        break
    k = k + 1
constant = (2*math.sqrt(2))/(9801)
print("Calculated pi: ", 1/(constant*result))
print("Real value: ",math.pi)