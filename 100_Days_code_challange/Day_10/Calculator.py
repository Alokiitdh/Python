print('--------------Calculator--------------')
# Function to permorm the calculator

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def divide(a,b):
    return a/b

cont = 'y'
while(cont == 'y'):
    solution = 0
    a = float(input('Enter a: '))
    b = float(input('Enter b: '))

    operation = input('''Enter operation:
             +
             -
             *
             /
          ''')
    if operation == '+':
        solution = add(a,b)
    elif operation == '-':
        solution = sub(a,b)
    elif operation == '*':
        solution = mul(a,b)
    else:
        if b == 0:
            print('Undefined')
        else:
            solution = divide(a,b)
    print(f'Solution: {solution}')
    cont = input('Want to continue(y/n)' )
    
    
