import pandas as pd

df = pd.DataFrame({
    'Name'  : ['  Alice ', 'BOB  ', 'carol', 'DAVID'],
'Email' : ['alice@GMAIL.COM', 'bob@yahoo.com', 'CAROL@hotmail.com',
'david@gmail.com'],
    'Phone' : ['9876543210', '987-654-3211', '(987)654-3212', '+91-987-654-3213']
})
print(df)

#Strip whitespace and standardize case
# df['Name'] = df['Name'].str.strip().str.title()
# df['Email'] = df['Email'].str.lower()
# print(df)


#Remove non-digit chars from phone
# df['Phone'] = df['Phone'].str.replace(r'[^0-9]', '', regex=True)
# print(df)


#Check if email contains '@'
# df['Valid_Email'] = df['Email'].str.contains('@')
# print(df)

#Extract domain from email
# df['Domain'] = df['Email'].str.split('@').str[1]
# print(df)