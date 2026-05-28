import pandas as pd
crm_data = pd.DataFrame({
    'Customer': [' john smith ', 'JANE DOE ', ' rachel Green', 'ross GELLER'],
    'Contact_No': ['123-456-7890', '(123) 456-7891', '+11234567892', '123.456.7893'],
    'Email_Addr': ['JOHN.S@NET.COM', 'jane.doe@work.org', 'Rachel@Gmail.com',
                   'ross@yahoo.com']
})
print(crm_data)
# print("Remove all spaces at the absolute start/end of strings in Customer, and cast them to standardized Title Case structure.")
# crm_data["Customer"] = crm_data["Customer"].str.strip().str.title()
# print(crm_data)

# print(
#     "Use a regular expression match string pattern ([^0-9]) to strip punctuation characters, leaving absolute digits.")
# crm_data["Contact_No"] = crm_data["Contact_No"].str.replace(
#     r'[^0-9]', '', regex=True)
# print(crm_data)

print("Convert the Email_Addr values to purely lowercase strings. Then split the email string at the @ symbol to populate a new column named Domain.")
crm_data["Email_Addr"] = crm_data["Email_Addr"].str.lower()
crm_data["Domain"] = crm_data["Email_Addr"].str.split('@').str[1]
print(crm_data)
