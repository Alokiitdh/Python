

def duplicate_unsorted(unsorted_array):
    result = []
    seen = set()

    for i in unsorted_array:
        if i not in seen:
            result.append(i)
            seen.add(i)
    result.sort()
    return result
array = [0,6,3,4,9,2,6,6,3,9,2,4,4,3,8]
result1 = duplicate_unsorted(array)
print('Output', result1)

    