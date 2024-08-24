#double day
from datetime import datetime, timedelta

def calculate_double_day(birthdate1, birthdate2):
    age_difference = birthdate2 - birthdate1
    double_day= birthdate2 + age_difference

    return double_day

birthdate1 = datetime(2010,3,15)
birthdate2 = datetime(2014, 6, 10)

d_day = calculate_double_day(birthdate1, birthdate2)
print(d_day)
