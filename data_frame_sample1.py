import pandas as pd

students = {
    'First Name': pd.Series(['Ibu', 'Diop', 'Tiano']),
    'Last Name': pd.Series(['Niang', "Real", 'City']),
    'Grades': pd.Series([67, 89, 45])
}

my_data = [{'x':10, 'y':20},
           {'x':55, 'y':33, 'z':22}]

df1 = pd.DataFrame(students)
df2 = pd.DataFrame(my_data, columns=['x', 'y', 'z'])
cols = list(df1.columns)

print(df1[:1])

