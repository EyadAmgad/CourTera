import pandas as pd 

df = pd.read_csv('coursera_course.csv')
print(df.columns)
df =df.drop(['Review counts'], axis=1)
df = df.drop(['Unnamed: 0'], axis=1)

print(df.columns)
print(df.head())
print(df.info())
df = df[0:10]
print(df)
df.to_csv('newcourses.csv')