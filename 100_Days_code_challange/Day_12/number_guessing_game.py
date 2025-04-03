print('''
 __    _  __   __  __   __  _______  _______  ______      _______  __   __  _______  _______  _______  ___   __    _  _______ 
|  |  | ||  | |  ||  |_|  ||  _    ||       ||    _ |    |       ||  | |  ||       ||       ||       ||   | |  |  | ||       |
|   |_| ||  | |  ||       || |_|   ||    ___||   | ||    |    ___||  | |  ||    ___||  _____||  _____||   | |   |_| ||    ___|
|       ||  |_|  ||       ||       ||   |___ |   |_||_   |   | __ |  |_|  ||   |___ | |_____ | |_____ |   | |       ||   | __ 
|  _    ||       ||       ||  _   | |    ___||    __  |  |   ||  ||       ||    ___||_____  ||_____  ||   | |  _    ||   ||  |
| | |   ||       || ||_|| || |_|   ||   |___ |   |  | |  |   |_| ||       ||   |___  _____| | _____| ||   | | | |   ||   |_| |
|_|  |__||_______||_|   |_||_______||_______||___|  |_|  |_______||_______||_______||_______||_______||___| |_|  |__||_______|
''')
import random

random_number = random.randint(1, 100)
#print(random_number)
count = 0
Choose_level = input('Enter level(Hard/Easy): ')
if Choose_level == 'Hard':
    level = 4
else:
    level = 9
while(count < level):
    number = int(input('Choose number: '))
    if number == random_number:
        print('Yeah!! You got the number')
        break
    elif number < random_number:
        print('Low')
    elif number > random_number:
        print('High')
    else:
        if number >= 100:
            print('Choose between 1 and 100')
            break
    count +=1

print(f'The number was: {random_number}')


