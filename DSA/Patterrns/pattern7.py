'''
            *
           ***
          *****
         *******
'''
row = 4
for i in range(0,row):
    for j in range(0,row-i-1):
        print('-',end='')
    for j in range(0,2*i+1):
        print('*', end='')
    print()
    
