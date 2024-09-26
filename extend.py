# on my machine, i ran this with:  
#   python3.13 -B extend.py ../moot/optimize/[comp]*/*.csv

import random, sys
from ezr import the, DATA, csv
import stats

dataset = sys.argv[1]

d = DATA().adds(csv(dataset))
b4 = [d.chebyshev(row) for row in d.rows]
low_dimensions_somes = []
high_dimensions_somes = []
(low_dimensions_somes if len(d.cols.x) < 6 else high_dimensions_somes).append(stats.SOME(b4,f"asIs,{len(d.rows)}"))

repeats = 1
for N in (20,30,40,50):
  the.Last = N
  d = DATA().adds(csv(dataset))
  dumb = [d.clone(random.choices(d.rows, k=N)).chebyshevs().rows for _ in range(repeats)]
  dumb = [d.chebyshev( lst[0] ) for lst in dumb]

  (low_dimensions_somes if len(d.cols.x) < 6 else high_dimensions_somes).append(stats.SOME(dumb,f"dumb,{N}"))

  the.Last = N
  smart = [d.shuffle().activeLearning() for _ in range(repeats)]
  smart = [d.chebyshev( lst[0] ) for lst in smart]
  (low_dimensions_somes if len(d.cols.x) <6 else high_dimensions_somes).append(stats.SOME(smart,f"smart,{N}"))

(stats.report(low_dimensions_somes, 0.01) if len(d.cols.x) < 6 else stats.report(high_dimensions_somes, 0.01))
