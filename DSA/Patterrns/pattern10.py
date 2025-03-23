'''
            *
            **
            ***
            ****
            ****
            ***
            **
            *
'''

for i in range(0,4):
    for j in range(0,i+1):
        print('*', end='')
    print()
temp = 4
for i in range(0,4):
    for j in range(0, temp):
        print('*', end='')
    temp-=1
    print()

