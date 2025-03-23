'''
1
0 1
1 0 1
0 1 0 1
1 0 1 0 1

'''
row = 5
for i in range(0 , row):
    for j in range(0, i+1):
        if (i+j)%2 == 0:
            print('1', end='')
        else:
            print('0', end='') 
    print()