print('Welcome to Rolar COaster ride\n')

price1 = 10
price2 = 7
price3 = 5
price4 = 3

height = int(input('Enter your height(cm): '))
age = int(input('Enter Your Age: '))
photo = input('Want photo(y/n): ')
if height >= 120:
    print('eligible')
    if age>= 18:
        #print(f'You have to pay : {price1}')
        temp = price1
    elif 12<=age<18:
       # print(f'you have to Pay: {price2}')
        temp = price2
    else:
        #print(f'Pay: {price3}')
        temp = price3
if photo == 'y':
    print(f'Total Pay: {price4+ temp}')
else:
    print('Not Eligible')