student_data = []
for _ in range(int(input('Enter number'))):
    name = input('Enter name')
    score = float(input('Enter Score'))
                
    student_data.append([name, score])
marks = 0
new = []
for student_score in student_data:
    for score in student_score:
        if score[1] > marks:
            student_data.append(new.append(score))
            
print(student_data)