def is_prime(num):
    if num == 0 or num == 1:
        return False
    else:
        count = 0
        for i in range(1,num+1):
            if num % i == 0:
                count += 1
        
    if count >2:
        return False
    else:
        return True
    


print(is_prime(10245762))