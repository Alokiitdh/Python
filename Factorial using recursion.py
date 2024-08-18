
n = int(input('Enter a number : '))

if n==0:
    print('1')
elif n<0:
    print('Factorial of negative number does not exist')

else:
    def factorial(n):
        if n==1:
            return 1
        else:
            return n*factorial(n-1)
fact = factorial(n)
print(fact)