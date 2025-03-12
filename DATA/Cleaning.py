import pandas as pd

df = pd.read_excel(r"URL")
df # to show the df

# Drop duplicates
df = df.drop_duplicates()

# Remove column
df = df.drop(columns = "Name of the column you want to delete")

# Modifying contents in a column
# strip for both sides
# lstrip for left side
# rstrip for right side
df["Column name to modify"] = df["Column name to modify"].str.lstrip("...") # Exemple to strip ... before a name
# need to do the strip one by one

# For phone numbers, good example
# If format is 123-456-7890
# the following will keep only alphabet and numbers
df["column name to modify"] = df["column name to modify"].str.replace('[^a-zA-Z0-9]','')
# Need to change to string before formating
df["column name to modify"] = df["column name to modify"].apply(lambda x: str(x))
df["column name to modify"] = df["column name to modify"].apply(lambda x: x[0:3]+'-'+ x[3:6]+'-'+ x[6:10])
df["column name to modify"] = df["column name to modify"].str.replace('value to replace','value wanted, can be blank')

# split columns for addresses for example 
# split : the number used is the number of separators to check
df[["Street address","State", "Zip_Code"]] = df["column to modify"].str.split(',',2, expand=True)

# Change Yes to Y and No to N
df["Column name to modify"] = df["Column name to modify"].str.replace('Yes','Y')
df["Column name to modify"] = df["Column name to modify"].str.replace('No','N')

# Clean N/A in entire DF
df.replace('N/A','')
# the following empty blanks
df.fillna('')

# Example Do not contact, if Yes, ignore
for x in df.index:
    if df.loc[x, "Do_Not_Contact"] == 'Y':
        df.drop(x, inplace=True)

# if phone number blank ignore
for x in df.index:
    if df.loc[x, "Phone_number"] == '':
        df.drop(x, inplace=True)

# or could have used dropna
df.dropna(subset="Phone_number", inplace=True)

# modifying new index (drop=true will ignore the new list)
df.reset_index(drop=True)