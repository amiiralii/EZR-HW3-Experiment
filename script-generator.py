import sys, os
from ezr import DATA, csv

def printscript(dataset, length):
  cwd = os.getcwd()
  if length == "low":
    print(f'python3.13 {cwd}/extend.py {cwd}/{dataset} | tee {cwd}/exp/res/low-dimension/{dataset.split("/")[-1]} &')
  else:
    print(f'python3.13 {cwd}/extend.py {cwd}/{dataset} | tee {cwd}/exp/res/high-dimension/{dataset.split("/")[-1]} &')

print(f"mkdir -p {os.getcwd()}/exp/res")
print(f"mkdir -p {os.getcwd()}/exp/res/low-dimension")
print(f"mkdir -p {os.getcwd()}/exp/res/high-dimension")
print(f"rm {os.getcwd()}/exp/res/low-dimension/*")
print(f"rm {os.getcwd()}/exp/res/high-dimension/*")

for i in os.listdir(f"data/optimize"):
  for j in os.listdir(f"data/optimize/{i}/"):
    if j[-4:] == ".csv":
      printscript(str("data/optimize/"+i+"/"+j), ("low" if len(DATA().adds(csv("data/optimize/"+i+"/"+j)).cols.x) < 6 else "high") )
  