student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

# accesing the element 
# from the dictionary
# is same as accesing in list
# but the main difference is .
# here in disctiory we have key 
# instead of index

# for key in student_scores:
# print(key)# this will print keys only
# print(student_scores[key])# it will print the key values

student_grades = {} # an empty dictionary for grading

for key in student_scores:
    if 91<= student_scores[key] <= 100:
        student_grades[key] = 'Outstanding'
    elif  81<= student_scores[key] <= 90:
        student_grades[key] = 'Exceeds Expectations'
    elif  71<= student_scores[key] <= 80:
        student_grades[key] = 'Acceptable'
    else:
        student_grades[key] = 'Fail'
   
print(student_grades)