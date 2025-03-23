print('Welcome to Pizza Deliveries')
size = input('What size pizza do u want(S, M or L): ')
pepperoni = input('Do You want pepperoni on your pizza (y/n): ')
extra_cheese = input('Do you want extra cheese(y/n): ')

# Prices according top the size:

S = 15
M = 20
L = 25

#price for peperoni
p_y= 2

#extra cheese price
p_cheese = 5

if size == 'S':
    temp = S
elif size == 'M':
    temp = M
else:
    temp = 'L'

if pepperoni == 'y':
    if extra_cheese == 'y':
        total_pay = temp + p_y + p_cheese
    else:
        total_pay = temp + p_y 
else:
    if extra_cheese == 'y':
        total_pay = temp + p_cheese
    else:
        total_pay = temp 


print(f'Total Bill: {total_pay}')