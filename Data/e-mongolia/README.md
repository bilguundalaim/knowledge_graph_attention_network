## Scripts

### `extract_bipartite_graph.py`
Read data from request.xlsx excel file and generate user-item interaction (bipartite) graph.

### `generate_kg.py`
Read data from agency.xlsx excel file and generate knowledge graph.

### `generate_lists.py`
Generate user and item lists with numerical IDs from train.raw.txt (bipartite graph).

### `generate_mappings.py`
Generate entity and relation mappings with numerical IDs from kg_final_raw.txt and item_list.txt files.

### `embedding.py`
Embed bipartite and knowledge graphs from previously generated mappings.

### `split_train.py`
Split train_raw.txt bipartite graph into 80% and 20%.

### Usage
```bash
python extract_bipartite_graph.py
python generate_kg.py
python generate_lists.py
python generate_mappings.py
python embedding.py
python split_train.py
