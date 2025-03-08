import pandas as pd

users = set()
services = set()

train_file = "../train_raw.txt"
with open(train_file, "r") as f:
  for line in f:
    parts = line.strip().split()
    user_id = parts[0]
    service_ids = parts[1:]
    
    users.add(user_id)
    services.update(service_ids)
      
user_mapping = {user: idx for idx, user in enumerate(sorted(users))}
service_mapping = {service: idx for idx, service in enumerate(sorted(services))}

with open("../user_list.txt", "w") as f:
  f.write("org_id remap_id\n")
  for user, idx in user_mapping.items():
    f.write(f"{user} {idx}\n")
    
with open("../item_list.txt", "w") as f:
  f.write("org_id remap_id\n")
  for service, idx in service_mapping.items():
    f.write(f"{service} {idx}\n")