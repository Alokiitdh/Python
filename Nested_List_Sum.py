# List
num = []

my_list =[[1,2],[3],[4,5,6]]

def nested_sum(my_list):
    sum = 0
    for i in range(len(my_list)):
        num = my_list[i]
        for k in range(len(num)):
            sum = sum + num[k]
    return(sum)

sum_List = nested_sum(my_list)
print(sum_List)