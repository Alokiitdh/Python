import random

word_list = ['machine', 'learning', 'python', 'coding', 'hoolooo', 'potato', 'tomato']

random_word = random.choice(word_list)
#print(random_word)
"""
# Alternate way to choose random word

random_index = random.randint(0, len(word_list)-1)
print(word_list[random_index])

"""
## Creating placeholder
placeholder = ''  # its a string placeholder

for position in range(len(random_word)):
    placeholder += '_'
print(placeholder)
placeholderlist = list(placeholder)


play_chances = len(random_word)+2


count =1

while(count>0 and play_chances != 0):

    guess= input('Enter a letter(lower_case): ')

    for letter in random_word:
        if letter == guess:
            for index in range(len(random_word)):
                if random_word[index]== guess:
                    placeholderlist[index] = guess
                    placeholder = ''.join(placeholderlist)
                    #print(placeholder)

    print(placeholder)
    if '_' not in placeholder:
        print('############### you Got the Word ############')
        print('****WON****')
        
    else: 
        play_chances -=1
        print(f'Chances Left: {play_chances}')
        if play_chances == 0:
            print('💀_____________Game Over____________💀')


    count = 0
    for dash in placeholder:
        if dash == '_':
           count+= 1



