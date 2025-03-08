import pandas as pd

# Reading data from excel file
print("Reading data from excel file...")
df_service = pd.read_excel('../excel-files/emon.service.xlsx')

# Creating a list to store the triples
kg_triples = []

# Iterating over the rows of the dataframe
print("Iterating over the rows of the dataframe...")
for index, row in df_service.iterrows():
  # Extracting the service_id and agency_id
  service_id = f"{row['_id']}"
  agency_id = f"{row['govAgencyId']}"
  
  # Appending the triple to the list with the format: service_id provided_by agency_id
  kg_triples.append(f"{service_id} provided_by {agency_id}")

# Writing the triples to a file
print("Writing the triples to a file...")
with open('../kg_final.txt', 'w') as f:
  for triple in kg_triples:
    f.write(triple + "\n")