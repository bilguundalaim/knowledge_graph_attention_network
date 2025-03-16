import pandas as pd

# Reading all sheets from the excel file
print("Reading all sheets from the excel file...")
all_sheets = pd.read_excel("../excel-files/request.xlsx", sheet_name=None)

# Concatenating all sheets
print("Concatenating all sheets...")
df = pd.concat(all_sheets.values())

# Dropping unnecessary columns
print("Dropping unnecessary columns...")
df = df[["userid", "service_id"]]

# Grouping by userid and concatenating service_id
print("Grouping by userid and concatenating service_id...")
train_data = df.groupby("userid")["service_id"].apply(lambda x: " ".join(map(str, x))).reset_index()

# Saving the data
print("Saving the data...")
train_data.to_csv("../train_raw.txt", sep=" ", index=False, header=False, escapechar=' ')