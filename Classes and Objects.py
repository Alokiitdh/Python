#Classes and Objects

class point:
    '''Represnts a point in 2D space'''

'''
Here header indicates new class is called point
'''    
blank = point()

blank.x = 3.0
blank.y = 4.0
print(blank)



class Time:
    '''Represent the time of the day(hours, minutes, seconds)'''

#assigning new time object for attributes

time = Time()
time.hour = 11
time.minutes = 59
time.second = 30

def print_time(time):
    print(f"{time.hour}:{time.minutes}:{time.second}")

print_time(time)