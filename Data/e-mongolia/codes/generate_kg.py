import pandas as pd

# Function to assign an age group based on the age
def assign_age_group(age):
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

# Reading data from excel file
print("Reading data from excel file...")
df_citizen = pd.read_excel('../excel-files/citizen.xlsx')
df_service = pd.read_excel('../excel-files/emon.service.xlsx')

# Creating a list to store the triples
kg_triples = []

# Iterating over the rows of the citizen dataframe
print("Iterating over the rows of the citizen dataframe...")
for index, row in df_citizen.iterrows():
    # Extracting the userid and age group
    user_id = f"{row['userid']}"
    age_group = assign_age_group(row['age'])
    
    # Appending the triple to the list with the format: user_id belongs_to age_group
    kg_triples.append(f'{user_id} belongs_to {age_group}')

# Iterating over the rows of the service dataframe
print("Iterating over the rows of the service dataframe...")
for index, row in df_service.iterrows():
    # Extracting the service_id and agency_id
    service_id = f"{row['_id']}"
    agency_id = f"{row['govAgencyId']}"
    
    # Appending the triple to the list with the format: service_id provided_by agency_id
    kg_triples.append(f"{service_id} provided_by {agency_id}")

# Writing the triples to a file
print("Writing the triples to a file...")
with open('../kg_final_raw.txt', 'w') as f:
    for triple in kg_triples:
        f.write(triple + "\n")