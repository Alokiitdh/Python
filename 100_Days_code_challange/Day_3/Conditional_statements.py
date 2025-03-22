print('Welcome to Rolar COaster ride\n')

height = int(input('Enter your height(cm): '))
age = int(input('Enter Your Age: '))
if height >= 120:
    print('eligible')
    if age>= 18:
        print('You have to pay : 10$')
    elif 12<=age<18:
        print('you have to Pay: 7$')
    else:
        print('Pay 5$')
else:
    print('Not Eligible')