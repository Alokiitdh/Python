# Cumulative Sum

my_list = [1,2,3,4]

def cum_sum(my_list):
    sum = 0
    for i in range(len(my_list)):
        sum = sum + my_list[i]
    return sum
print(cum_sum(my_list))    
