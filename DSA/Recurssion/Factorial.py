def fact(n):
    if n==1 or n==0:
        return 1
    elif n<0:
        return 'Factorial not defined'
    else:
        return n* fact(n-1)
    
    
n = 3
fac = fact(n)
print(f'{fac}')