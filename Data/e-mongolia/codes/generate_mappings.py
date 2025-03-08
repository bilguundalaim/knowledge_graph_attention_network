import pandas as pd

kg_file = "../kg_final.txt"

# Initialize sets to store entities and relations
entities = set()
relations = set()

# Read kg_final.txt and extract entities and relations
print("Reading knowledge graph from kg_final.txt file...")
with open(kg_file, 'r') as f:
  for line in f:
    parts = line.strip().split()
    if len(parts) == 3:
      entities.add(parts[0])
      relations.add(parts[1])
      entities.add(parts[2])

# Assign unique ids to each entity and relation
print("Assigning unique ids to entities and relations...")
entity_mapping = {entity: idx for idx, entity in enumerate(sorted(entities))}
relation_mapping = {relation: idx for idx, relation in enumerate(sorted(relations))}

# Write entity and relation mappings to files
print("Writing entity and relation mappings to files...")
with open("../entity_list.txt", "w") as f:
  for entity, idx in entity_mapping.items():
    f.write(f"{entity} {idx}\n")
    
with open("../relation_list.txt", "w") as f:
  for relation, idx in relation_mapping.items():
    f.write(f"{relation} {idx}\n")