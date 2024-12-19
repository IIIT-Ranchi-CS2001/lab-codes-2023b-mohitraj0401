import pandas as pd
import numpy as np

file_path = "AQI_Data.csv"  
data = pd.read_csv(file_path)


print("First 8 rows:")
print(data.head(8))


print("\nLast 5 rows:")
print(data.tail(5))


print("\nColumn Data Types and Non-Null Values:")
print(data.info())  



city_stats = data.groupby('City').agg({
    'AQI': np.mean,
    'PM2.5': np.max,
    'PM10': np.min
}).reset_index()

print("\nCity-wise statistics:")
print(city_stats)




pivot_table = pd.pivot_table(data, values='PM2.5', index='City', aggfunc='max')


print(pivot_table)


pivot_table.to_csv('pivot.csv', index=True)



