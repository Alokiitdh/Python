import random

word_list = ['machine', 'learning', 'python', 'coding']

random_word = random.choice(word_list)
print(random_word)
"""
# Alternate way to choose random word

random_index = random.randint(0, len(word_list)-1)
print(word_list(random_index))

"""
## Creating placeholder
placeholder = ''  # its a string placeholder

for position in range(len(random_word)):
    placeholder += '_'
print(placeholder)



guess= input('Enter a letter(lower_case): ')

for letter in random_word:
    if letter == guess:
        for index in range(len(random_word)):
            if random_word[index]== guess:
                placeholder[index] = guess
    else:
        pass
        

print(placeholder)