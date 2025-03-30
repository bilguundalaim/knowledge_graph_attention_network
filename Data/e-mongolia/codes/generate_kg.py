import pandas as pd
import os

# Function to assign an age group based on the age
def assign_age_group(age):
    if pd.isna(age) or not isinstance(age, (int, float)):
        return "unknown"
    if age < 27:
        return "under_27"
    elif age < 35:
        return "27_34"
    elif age < 42:
        return "35_41"
    elif age < 51:
        return "42_50"
    elif age < 61:
        return "51_60"
    else:
        return "over_60"

# Reading data from Excel files
print("Reading data from Excel files...")
df_citizen = pd.read_excel('../excel-files/citizen.xlsx')
df_service = pd.read_excel('../excel-files/emon.service.xlsx')
df_request = pd.read_excel('../excel-files/request.xlsx')

# Ensure 'createc_date' column exists and convert to datetime
if 'createc_date' in df_request.columns:
    df_request = df_request.copy()
    df_request.loc[:, 'createdDate'] = pd.to_datetime(df_request['createc_date'])
else:
    raise KeyError("Column 'createc_date' not found in request.xlsx")

# Creating a list to store the triples
kg_triples = []

# Adding user belongs_to age group triples
print("Adding user belongs_to age group triples from citizen dataframe")
df_citizen['age_group'] = df_citizen['age'].apply(assign_age_group)
kg_triples.extend(df_citizen.apply(lambda row: f"{row['userid']} belongs_to {row['age_group']}", axis=1))

# Adding service provided_by gov agency triples
print("Adding service provided_by gov agency triples from service dataframe")
kg_triples.extend(df_service.apply(lambda row: f"{row['_id']} provided_by {row['govAgencyId']}", axis=1))

# Adding request belongs_to service triples
# Adding request created_on month triples
print("Adding request belongs_to service and created_on month triples from request dataframe")
kg_triples.extend(df_request.apply(lambda row: f"{row['requestid']} belongs_to {row['service_id']}", axis=1))
kg_triples.extend(df_request.apply(lambda row: f"{row['requestid']} created_on {row['createdDate'].month}", axis=1))

# Writing the triples to a file
output_file = '../kg_final_raw.txt'
os.makedirs(os.path.dirname(output_file), exist_ok=True)
print("Writing the triples to a file...")
with open(output_file, 'w') as f:
    for triple in kg_triples:
        f.write(triple + "\n")