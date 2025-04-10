import pandas as pd

students_data = {
    'Student_1': {'name': 'Alice', 'marks': 85},
    'Student_2': {'name': 'Bob', 'marks': 78},
    'Student_3': {'name': 'Charlie', 'marks': 92},
    'Student_4': {'name': 'David', 'marks': 74},
    'Student_5': {'name': 'Eve', 'marks': 88}
}

data = pd.DataFrame(students_data)
print(data)