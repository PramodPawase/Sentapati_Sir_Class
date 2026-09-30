import pandas as pd

# Excel फाइल वाचण्यासाठी openpyxl लागते
# जर install नसेल तर आधी install कर:
# pip install openpyxl

# Excel फाइल वाचणे
emp = pd.read_excel(
    r"C:/Users/Pramod/OneDrive/AI Python/Senapati Sir/Class Document/30th_sep_class/Rawdata.xlsx"
)

# पहिले 5 rows दाखवणे
print(emp.head())

# DataFrame ची माहिती
print(emp.info())

# संपूर्ण डेटा print करणे
print(emp)
print('=================')
print('\n')
print(emp[['Name','Age']])

print('=================')
print('\n')

emp_age=emp['Age'].str.replace('r\W','',regex=True)
print(emp_age)

print('=================')
print('\n')

emp_digit=emp['Age'].str.extract('(\d+)')
print(emp_age)

print('=================')
print('\n')

emp_location=emp['Age'].str.replace('r\W','')
print(emp_location)

emp_age_Lc=emp['Location'].str.replace('r\W','',regex=True)
print(emp_age_Lc)

emp_age_Exp=emp['Exp'].str.replace('r\W','',regex=True)
print(emp_age_Lc)


print('=================')
print('\n')

clean_data=emp.copy()
print(clean_data)


print('======EDA Technique===========')
print('\n')

