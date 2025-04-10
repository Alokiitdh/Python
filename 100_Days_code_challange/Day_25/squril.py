import pandas as pd
dataframe = pd.read_csv(r'C:\Users\alokj\OneDrive\Documents\GitHub\Python\Data_sets\2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20250410.csv')
updated_frame = dataframe['Primary Fur Color']
gray_sq = (updated_frame == 'Gray').sum()
red_sq = (updated_frame == 'Cinnamon').sum()
black_sq = (updated_frame == 'Black').sum()
print(f'Gray: {gray_sq}')
print(f'Red: {red_sq}')
print(f'Black: {black_sq}')

data_dict = {
    'color': ['Gray', 'Cinnamon', 'Black'],
    'Count': [gray_sq, red_sq, black_sq]

}
sq_frame =pd.DataFrame(data_dict)
print(sq_frame)
