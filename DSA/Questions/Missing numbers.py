
def missng_number(array):
    n = len(array) # number of elements in tha array and n is the range number
    expected_sum = n*(n+1)/2
    original_sum = sum(array)
    missing_number = expected_sum-original_sum
    return missing_number

array = [0,3,1]
mising=missng_number(array)
print('missing number: ', int(mising))
