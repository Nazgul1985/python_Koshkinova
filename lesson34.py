import pandas as pd 

data ={'Name':['Nazgul','Ascar','Azamat','Nadia', 'Kausar'],
       'Age': [39,39,14,12,6],
       'Gender':['Z','M','M','Z','Z'],
       'GPA':[5,3,5,5,5]
}
df= pd.DataFrame(data)
print (df)
print(df['Name'])
z_pol = df[df['Gender'] == 'Z']
print(z_pol)

max_gpa_student = df[df['GPA'] == df['GPA'].max()]
print(max_gpa_student)

df['Age'] = df['Age'] + 1
print(df)

min_age = df['Age'].min()
df.loc[df['Age'] == min_age, 'GPA'] = 4.0
print(df)

new_student = {'Name': 'Talgat', 'Age': 20, 'Gender': 'M', 'GPA': 2}
df = df.append(new_student, ignore_index=True)
print(df) 