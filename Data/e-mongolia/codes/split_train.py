import pandas as pd
import random

input_train = "../train_embedded.txt"
output_train = "../train.txt"
output_test = "../test.txt"

with open(input_train, "r") as f:
  lines = f.readlines()
  
random.shuffle(lines)

split_idx = int(len(lines) * 0.8)
train_lines = lines[:split_idx]
test_lines = lines[split_idx:]

with open(output_train, "w") as f:
  f.writelines(train_lines)
  
with open(output_test, "w") as f:
  f.writelines(test_lines)