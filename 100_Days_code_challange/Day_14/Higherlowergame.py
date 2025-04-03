from Game_data import data
import random

loose = 0
score = 0
while(loose != 1):
    random_index_1 = random.randint(1,len(data))
    random_index_2 = random.randint(1,len(data))

    A = data[random_index_1]
    B = data[random_index_2]

    print(f'Compare A: {A['name']}, a {A['description']}, from {A['country']}')
    print(f'Compare B: {B['name']}, a {B['description']}, from {B['country']}')

    question = input('Tell who is having follower count(A/B): ')

    more_follower = ''

    if A['follower_count'] > B['follower_count']:
        more_follower = 'A'
    else:
        more_follower = 'B'

    if question == more_follower:
        print('You won')
        score += 1

    else:
        print('Try Again')
        loose +=1

print(f'Your Total Score is: {score}')
print(f'The correct was: {more_follower}')

# print(A)
# print('\n')
# print(B)
# dat is a list of dictionaries 
# for dict_ in data:# here basically we are getting each distionary
#     for key in dict_:# we entered in the first dictionary
#         if key == 'follower_count':
#             print(dict_[key])