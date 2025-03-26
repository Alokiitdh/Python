

# love_letters = ['t','r','u','e','l','o','v','e']

# def calculate_love_score(name1, name2):
#     count1=0
#     count2=0
#     if name1 == 'potato' and name2 == 'tomato':
#         print(f'Love Score: "Build by heaven cannot calculate" ')
#     else: 
#         for char in name1:
#             if char in love_letters :
#                 count1+=1
    
#         for  char in name2:
#             if char in love_letters:
#                 count2+=1

#         love_score = int(str(count1)+ str(count2))

#         print(f'Love Score: {love_score}')

# name1 = input('Enter Your name: ')
# name2 = input('Enter Your Love name: ')


# calculate_love_score(name1, name2)

Truee = ['t','r','u','e']
Love = ['l','o','v','e']

def calculate_love_score(name1, name2):
    count1=0
    count2=0

    for char in name1.lower():
        if char in Truee :
            count1+=1
            
    for char in name2.lower():
        if char in Truee :
            count1+=1
    
    for  char in name1.lower():
        if char in Love:
            count2+=1
            
    for  char in name2.lower():
        if char in Love:
            count2+=1

    love_score = int(str(count1)+ str(count2))

    print(love_score)

# name1 = input('Enter Your name: ')
# name2 = input('Enter Your Love name: ')


calculate_love_score("Kanye West", "Kim Kardashian")