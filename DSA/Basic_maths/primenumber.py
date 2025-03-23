number = int(input('Enter number: '))

num = number

if num <=1:
    print('Not a Prime number')
else:
    for i in range(2, num):
        if num%i ==0:
            print(' Not a Prime')
            break
    else: 
        print('Prime')
            

