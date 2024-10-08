class Time:
    '''Class for time'''

start = Time() # Created a Start object
start.hour = 9
start.minute = 45
start.seconds = 00

duration = Time() # created a duration object
duration.hour = 1
duration.minute = 35
duration.seconds = 00

def print_time(t):
    print(f"{t.hour:02d}':'{t.minute:02d}':'{t.seconds:02d}")
    
def add_time(t1, t2):
    sum = Time() # new object fo the summation of the time
    sum.hour = t1.hour + t2.hour
    sum.minute = t1.minute + t2.minute
    sum.seconds = t1.seconds + t2.seconds

    #removing the problem 
    '''This function does not deal with the case where the number of seconds or minutes adds up to more than sixty'''

    if sum.seconds >= 60:
        sum.seconds -= 60
        sum.minute += 1
    if sum.minute >= 60:
        sum.minute -= 60
        sum.hour += 1
    return sum

done = add_time(start, duration)
print_time(done)