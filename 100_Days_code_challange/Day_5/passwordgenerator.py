import random

capital_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
                   'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

small_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
                 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

special_characters = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', 
                      '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', 
                      '_', '`', '{', '|', '}', '~']

print('Welcome to the PyPassword Generators!!')
cap_letters = int(input('How many Capital letters: '))
sm_letters = int(input('How many Small letters: '))
num = int(input('How many numbers: '))
symb = int(input('How many symmbols: '))

# make an empty list and shuffle it

password = []

for char in range(0, cap_letters):
    random_char = random.choice(capital_letters)
    password += random_char

for char in range(0, sm_letters):
    random_char = random.choice(small_letters)
    password+= random_char

for num in range(0, num):
    random_char = random.choice(numbers)
    password+= random_char

for char in range(0, symb):
    random_char = random.choice(special_characters)
    password+= random_char

print(password)
random.shuffle(password)
print(password)

passwordstr = ''

for char in password:
    passwordstr+=char

print(passwordstr)