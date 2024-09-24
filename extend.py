# on my machine, i ran this with:  
#   python3.13 -B extend.py ../moot/optimize/[comp]*/*.csv

import random
from ezr import the, DATA, csv, dot, chebyshevs
import stats
from math import exp
import time

d = DATA().adds(csv("data/optimize/misc/auto93.csv"))
b4 = [d.chebyshev(row) for row in d.rows]
low_dimensions_somes = [stats.SOME(b4,f"asIs,{len(d.rows)}")]
high_dimensions_somes = [stats.SOME(b4,f"asIs,{len(d.rows)}")]

repeats = 20
for N in (20,30,40,50):
  the.Last = N
  d = DATA().adds(csv("data/optimize/misc/auto93.csv"))
  dumb = [d.clone(random.choices(d.rows, k=N)).chebyshevs().rows for _ in range(repeats)]
  dumb = [d.chebyshev( lst[0] ) for lst in dumb]

  (low_dimensions_somes if len(d.cols.x) < 6 else high_dimensions_somes).append(stats.SOME(dumb,f"dumb,{N}"))

  the.Last = N
  smart = [d.shuffle().activeLearning() for _ in range(repeats)]
  smart = [d.chebyshev( lst[0] ) for lst in smart]
  (low_dimensions_somes if len(d.cols.x) else high_dimensions_somes).append(stats.SOME(smart,f"smart,{N}"))

stats.report(low_dimensions_somes, 0.01)
print('\n\n')
stats.report(high_dimensions_somes, 0.01)

#-------------------------------------------------------------------------------
'''
d = DATA().adds(csv("data/optimize/misc/auto93.csv"))
b4 = [d.chebyshev(row) for row in d.rows]
somes = [stats.SOME(b4,f"asIs,{len(d.rows)}")]
print(len(b4))

rnd = lambda z: z
scoring_policies = [
  ('exploit', lambda B, R,: B - R),
  ('explore', lambda B, R :  (exp(B) + exp(R))/ (1E-30 + abs(exp(B) - exp(R))))]
repeats = 1

for what,how in scoring_policies:
  for the.Last in [0,20, 30, 40]:
    for the.branch in [False, True]:
      start = time.time()
      result = []
      runs = 0
      for _ in range(repeats):
         tmp=d.shuffle().activeLearning(score=how)
         runs += len(tmp)
         result += [rnd(d.chebyshev(tmp[0]))]

      pre=f"{what}/b={the.branch}" if the.Last >0 else "rrp"
      tag = f"{pre},{int(runs/repeats)}"
      print(tag, f": {(time.time() - start) /repeats:.2f} secs")
      somes +=   [stats.SOME(result,    tag)]
      print((result))
      input()

stats.report(somes, 0.01)
'''