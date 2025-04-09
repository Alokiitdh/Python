from prettytable import PrettyTable

table = PrettyTable()
print(table)
# table.add_autoindex()
table.add_column('Studetn Name', ['Mohit', 'Rohit', 'Sohit'])
table.add_column('Marks', [23,56,78])
print(table)