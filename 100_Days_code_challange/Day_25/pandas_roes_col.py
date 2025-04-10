import pandas as pd
data_frame = pd.read_csv(r'C:\Users\alokj\OneDrive\Documents\GitHub\Python\100_Days_code_challange\Day_25\weather_data.csv')
print(data_frame)
# print(type(data_frame))
# temp_list = data_frame['temp'].to_list()
# print(temp_list)

# def avg_temp(temp):
#     total_values = len(temp)
#     sum = 0
#     for i in temp:
#         sum = sum+i

#     avg = sum / total_values
#     return avg

# print(f'Avg Temp : {avg_temp(temp_list):.2f}')

# print(data_frame['temp'].mean())
# ## Getting row data
# print(data_frame[data_frame.temp == data_frame.temp.max()])


## coverting temperatin

monday = data_frame[data_frame.day == 'Monday']
temp_mon = monday.temp[0]
temp_faren = (temp_mon *(9/5))+32


