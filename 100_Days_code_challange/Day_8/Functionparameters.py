def life_in_weeks(age):
    if age > 90:
        print('Enter valid age')
    else:
        new_age = 90-age
        weeks_left = new_age*52
        print(f'You have {weeks_left} weeks left.')


life_in_weeks(12)




