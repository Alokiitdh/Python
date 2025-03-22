print('Welcome to TIP calculator\n')
bill = float(input('What was the total bill: '))
tip_percentage = int(input('How much tip you want to give(10,12 or 15): '))
total_nil_with_tip = bill*((100+tip_percentage)/100)
split = int(input('How many people to split the bill: '))
individual_bill = total_nil_with_tip/split
print(f'Each person should pay: {round(individual_bill, 2)}')