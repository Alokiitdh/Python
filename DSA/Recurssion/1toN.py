def One_to_N(n, current = 1):
    if n<current:
        return
    else:
        print(current)
    One_to_N(n, current+1)


n =10
One_to_N(n)


## Alternate approach

def one(n):
    if n<=0:
        return
    else:
        one(n-1)
    print(n)

n =5
one(n)

## Reverse order
def oner(n):
    if n<= 0:
        return 
    else:
        print(n)
    oner(n-1)

n= 5
oner(n)