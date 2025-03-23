'''
            12345
            1234
            123
            12
            1
'''
temp = 5
for i in range(0,5):
    for j in range(0,temp):
        print(j+1, end='')
    temp-=1
    print()
