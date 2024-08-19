#Ackermann Function
print("Enter the Values for m and n For Ackermann Function:")
m = int(input("m: "))
n = int(input("n: "))


def ackermann(m,n):
    if m ==0:
        return n+1
    elif m > 0 and n == 0:
        return ackermann(m-1, 1) 
    elif m >0 and n > 0:
        return ackermann(m-1, ackermann(m, n-1))


ack = ackermann(m,n)
print(ack)


