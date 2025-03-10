import pandas as pd

kg_file = "../kg_final_raw.txt"
item_list_file = "../item_list.txt"

item_map = pd.read_csv(item_list_file, sep=" ", header=0, names=["org_id", "remap_id"], dtype=str)
item_dict = dict(zip(item_map["org_id"], item_map["remap_id"])) 

print("Max id in item_list: ", max(map(int, item_dict.values())))

# Initialize sets to store entities and relations
entities = set()
relations = set()

# Read kg_final_raw.txt and extract entities and relations
print("Reading knowledge graph from kg_final_raw.txt file...")
with open(kg_file, 'r') as f:
  for line in f:
    parts = line.strip().split()
    if len(parts) == 3:
      entities.add(parts[0])
      relations.add(parts[1])
      entities.add(parts[2])

# Assign unique ids to each entity and relation
print("Assigning unique ids to entities and relations...")

entity_mapping = {}
next_id = max(map(int, item_dict.values())) + 1

for entity in sorted(entities):
    if entity in item_dict:
        entity_mapping[entity] = item_dict[entity]
    else:
        entity_mapping[entity] = str(next_id)
        next_id += 1

relation_mapping = {relation: idx for idx, relation in enumerate(sorted(relations))}

# Write entity and relation mappings to files
print("Writing entity and relation mappings to files...")
with open("../entity_list.txt", "w") as f:
  f.write("org_id remap_id\n")
  for entity, idx in entity_mapping.items():
    f.write(f"{entity} {idx}\n")
    
with open("../relation_list.txt", "w") as f:
  f.write("org_id remap_id\n")
  for relation, idx in relation_mapping.items():
    f.write(f"{relation} {idx}\n")