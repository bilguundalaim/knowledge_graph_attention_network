import pandas as pd

user_map = pd.read_csv("../user_list.txt", sep=" ", header=None, names=["org_id", "remap_id"], dtype=str)
user_dict = dict(zip(user_map["org_id"], user_map["remap_id"]))

item_map = pd.read_csv("../item_list.txt", sep=" ", header=None, names=["org_id", "remap_id"], dtype=str)
item_dict = dict(zip(item_map["org_id"], item_map["remap_id"]))

entity_map = pd.read_csv("../entity_list.txt", sep=" ", header=None, names=["org_id", "remap_id"], dtype=str)
entity_dict = dict(zip(entity_map["org_id"], entity_map["remap_id"]))

relation_map = pd.read_csv("../relation_list.txt", sep=" ", header=None, names=["org_id", "remap_id"], dtype=str)
relation_dict = dict(zip(relation_map["org_id"], relation_map["remap_id"]))

input_train = "../train_raw.txt"
output_train = "../train.txt"

with open(input_train, "r") as fin, open(output_train, "w") as fout:
  for line in fin:
    parts = line.strip().split()
    user = user_dict.get(parts[0], None)
    items = [item_dict.get(part, None) for part in parts[1:]]
    
    if user is not None and all(items):
      fout.write(f"{user} {' '.join(items)}\n")
      
input_kg = "../kg_final_raw.txt"
output_kg = "../kg_final.txt"

with open(input_kg, "r") as fin, open(output_kg, "w") as fout:
  for line in fin:
    parts = line.strip().split()
    if len(parts) == 3:
      head = entity_dict.get(parts[0], None)
      relation = relation_dict.get(parts[1], None)
      tail = entity_dict.get(parts[2], None)
      
      if head is not None and relation is not None and tail is not None:
        fout.write(f"{head} {relation} {tail}\n")