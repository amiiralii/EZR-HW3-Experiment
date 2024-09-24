import sys, os

def printscript(dataset):
  cwd = os.getcwd()
  print(f'python3.13 {cwd}/extend.py {cwd}/{dataset} | tee {cwd}/{str.replace(dataset, "data/optimize", "exp/res")} &')

for i in os.listdir(f"data/optimize"):
  for j in os.listdir(f"data/optimize/{i}/"):
    if j[-4:] == ".csv":
      printscript(str("data/optimize/"+i+"/"+j))
  
[printscript(arg) for arg in sys.argv if arg[-4:] == ".csv"]
