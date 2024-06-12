import pandas as pd

mapeo = {-1: 'branch1', 0: 'branch2', 1: 'branch3'}
#types_dict = {'B': object}
#data = pd.read_csv('datos.csv', delimiter=';', dtype=types_dict)
data = pd.read_csv('datos.csv', delimiter=',')
print(data)
#print(data.columns)

#print(data['ColumnaB'])

#data = data.astype({'B': object})
print(data.info(verbose=True, show_counts=True))

col = 'B'
if col in data.columns:
    print("Column", col, "exists in the DataFrame.")
else:
    print("Column", col, "does not exist in the DataFrame.")

#data['B'] = data['A'].replace(mapeo)
print(data)