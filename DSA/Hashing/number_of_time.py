## Finding the duplicate and 
def duplicate(data):
    data_dict = {}
    for ele in data:
        if ele not in data_dict:
            data_dict[ele] = 1
        else:
            data_dict[ele] +=1

    return data_dict

def count_print(dict_):
    for ele, frq in dict_.items():
        if frq >= 1:
            print(f'{ele} => {frq}')

# counting the lowest and highest count
def high_low(dict_):
    max = 0
    for key, value in dict_.items():
        if value >= max:
            max = value
    i=1

    for key, value in dict_.items():
        if value == max:
            print(f'Highest {i}: {key}')
            i+=1

    print(max)
    j = 1  
    for key, value in dict_.items():
        min = max
        if value < min:
            min= value

    for key, value in dict_.items():
        if value == min:
            print(f'Lowest {j} = {key}')
            j+=1


data = [10,5,10,15,5,10,5]
bata = ['s','a','s','a']

dupi = duplicate(data)
count_print(dupi)
high_low(dupi)








