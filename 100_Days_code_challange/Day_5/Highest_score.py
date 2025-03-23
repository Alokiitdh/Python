student_score = [23,45,67,34,99,47,34]

## Finding the highest umber
max_score = 0
for score in student_score:
    if score > max_score:
        max_score = score
print(max_score)