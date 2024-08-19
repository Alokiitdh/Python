# Calculator
def sum(a,b):
    return a+b
def mul(a,b):
    return a*b
def div(a,b):
    if b==0:
        print('invalid')
    else: 
        return a/b
def sub(a,b):
    return a-b

a=float(input("Enter a:"))
b=float(input("Enter b:"))

print("Enter Choice: (+,*,/,-)")
choice = input()

if choice == '+':
    s=sum(a,b)
    print(s)
elif choice == '*':
    m=mul(a,b)
    print(m)
elif choice == '/':
    d=div(a,b)
    print(d)
else: 
    e=sub(a,b)
    print(e)