import pandas as pd
import csv

# Load User-Service Interaction Data
print("Reading all sheets from the excel file...")
all_sheets = pd.read_excel("../excel-files/request.xlsx", sheet_name=None)

# Concatenating all sheets
print("Concatenating all sheets...")
df = pd.concat(all_sheets.values())

# Dropping unnecessary columns
print("Dropping unnecessary columns...")
df = df[["userid", "service_id"]]

# Filtering unique service IDs that have been used at least once
used_services = set(df["service_id"].unique())

# Grouping by userid and concatenating service_id
print("Grouping by userid and concatenating service_id...")
train_data = df.groupby("userid")["service_id"].apply(lambda x: " ".join(map(str, x))).reset_index()

# Saving the filtered training data
print("Saving the training data...")
train_data.to_csv("../train_raw.txt", sep=" ", index=False, header=False, quoting=csv.QUOTE_NONE, escapechar=' ')

# Load Service Data and Filter Unused Services
print("Reading service data from excel file...")
df_service = pd.read_excel('../excel-files/emon.service.xlsx')

# Filtering services that are in the used_services set
df_service_filtered = df_service[df_service['_id'].astype(str).isin(used_services)]

# Creating a list to store the filtered knowledge graph triples
kg_triples = []

# Iterating over the filtered rows of the dataframe
print("Iterating over the filtered rows of the dataframe...")
for _, row in df_service_filtered.iterrows():
    service_id = f"{row['_id']}"
    agency_id = f"{row['govAgencyId']}"
    
    # Appending the valid triple
    kg_triples.append(f"{service_id} provided_by {agency_id}")

# Writing the filtered triples to a file
print("Writing the filtered triples to a file...")
with open('../kg_final_raw.txt', 'w') as f:
    for triple in kg_triples:
        f.write(triple + "\n")

print("Knowledge graph generation completed successfully.")
