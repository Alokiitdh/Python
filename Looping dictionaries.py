#Looping dictionaries
my_dict = {
    'one': 'Uno', 'two':'Puno', 'Three':'Duno' 
}

print(my_dict.values())
# Adding elemnet to the dictonary

my_dict['Four'] = 'Tuno'
print(my_dict)

def my_dictt(my_dict):
    for key in my_dict:
        print(key, ':',   my_dict[key])

my_dictt(my_dict)
