import matplotlib.pyplot as plt
import pandas as pd
from math import pi
import math as mt
from google.colab import files

#creating the dataframe
file1 = pd.read_csv("/content/Walkability.csv")
file2 = pd.read_csv("/content/Change_score.csv")
file3 = pd.read_csv("/content/Comfort_score.csv")
file4 = pd.read_csv("/content/Livability.csv")
file5 = pd.read_csv("/content/MedianAge.csv")
file6 = pd.read_csv("/content/Rsme_score.csv")
file7 = pd.read_csv("/content/Population.csv")
file8 = pd.read_csv("/content/pop_score.csv")

df1 = pd.DataFrame(file1)
df2 = pd.DataFrame(file2)
df3 = pd.DataFrame(file3)
df4 = pd.DataFrame(file4)
df5 = pd.DataFrame(file5)
df6 = pd.DataFrame(file6)
df7 = pd.DataFrame(file7)
df8 = pd.DataFrame(file8)

df1.set_index('Unnamed: 0', inplace=True)
df2.set_index('Unnamed: 0', inplace=True)
df3.set_index('Unnamed: 0', inplace=True)
df4.set_index('Unnamed: 0', inplace=True)
df5.set_index('Unnamed: 0', inplace=True)
df6.set_index('Unnamed: 0', inplace=True)
df7.set_index('Unnamed: 0', inplace=True)
df8.set_index('Unnamed: 0', inplace=True)

df2 = df2.mul(10)
df3 = df3.mul(10)
df5 = df5.mul(10)
df6 = df6.mul(10)
df8 = df8.mul(10)

df = df1.merge(df2, left_index=True, right_index=True)
df = df.merge(df3, left_index=True, right_index=True)
df = df.merge(df4, left_index=True, right_index=True)
df = df.merge(df5, left_index=True, right_index=True)
df = df.merge(df6, left_index=True, right_index=True)
df = df.merge(df7, left_index=True, right_index=True)
df = df.merge(df8, left_index=True, right_index=True)

col = ['Walkabilty', 'Change Score', 'Comfort Score', 'Livability', 'Median Age', 'RMSE', 'Population Change', 'Population']
df.columns = col

def area(x, y):
        n = len(x)
        s = 0.0
        for i in range(-1, n-1):
            s += x[i]*y[i+1] - y[i]*x[i+1]
        return abs(0.5*s)


areas = {}
# number of variables
categories=list(df)[0:]
N = len(categories)


#df.reset_index(drop=True, inplace=True)
angle_list = [0,45,90,135,180,225,270,315]

# What will be the angle of each axis in the plot? (we divide the plot / number of variable)
angles = [n / float(N) * 2 * pi for n in range(N)]
angles += angles[:1]

for i, row in df.iterrows(): 
  # We are going to plot the first line of the data frame.
  # But we need to repeat the first value to close the circular graph:
  values=df.loc[i].values.flatten().tolist()
  values += values[:1]
  values

  x = []
  y = []
  temp_values = values[:-1]
  
  for index in range(len(temp_values)):
    x.append(temp_values[index]*mt.cos(angle_list[index]))
    y.append(temp_values[index]*mt.sin(angle_list[index]))

  areas[i] = area(x, y)

tally = pd.DataFrame.from_dict(areas, orient='index')
tally.to_csv("nonneg.csv")
files.download("nonneg.csv")
#Getting Top ten spider charts from CSV
zips = [48207, 38109, 23666, 46406, 88310, 30906, 76522, 74126, 28358, 79912, 73013, 67601, 66607, 78840, 73942, 37410, 74012]

i = 0
for index, row in df.iterrows():
  if(index not in zips):
    df.drop(index, inplace=True)

print(df)
