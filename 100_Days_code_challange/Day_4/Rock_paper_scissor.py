import random
print('ROCK---PAPER--SCISSORS\n')

print('''What do you choose : 
        0: ROCK
        1: Paper
        2: Scissor''')

item = ['Rock', 'Paper', 'Scissor']

random_index = random.randint(0,2)
computer_choice = item[random_index]

my_choice = int(input('Enter Your Choice: '))

print(item[my_choice])
print(computer_choice)

if item[my_choice] == computer_choice:
    print('you Won')
else:
    print('Try Again')