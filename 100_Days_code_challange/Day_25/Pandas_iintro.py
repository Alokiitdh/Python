# with open(r'C:\Users\alokj\OneDrive\Documents\GitHub\Python\100_Days_code_challange\Day_25\weather_data.csv', mode ='r') as csv_data:
#     csv_data_list = csv_data.readlines()
#     print(csv_data_list)

import pandas as pd
data_frame = pd.read_csv(r'C:\Users\alokj\OneDrive\Documents\GitHub\Python\100_Days_code_challange\Day_25\weather_data.csv')
print(data_frame)
print("Temperature")
print(data_frame['temp'])