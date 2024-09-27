import random, sys
from ezr import the, DATA, csv
import stats

dataset = sys.argv[1]

d = DATA().adds(csv(dataset))
b4 = [d.chebyshev(row) for row in d.rows]
somes = []
somes.append(stats.SOME(b4,f"asIs,{len(d.rows)}"))

repeats = 20
for N in (20,30,40,50):
  the.Last = N
  d = DATA().adds(csv(dataset))
  dumb = [d.clone(random.choices(d.rows, k=N)).chebyshevs().rows for _ in range(repeats)]
  dumb = [d.chebyshev( lst[0] ) for lst in dumb]

  somes.append(stats.SOME(dumb,f"dumb,{N}"))

  the.Last = N
  smart = [d.shuffle().activeLearning() for _ in range(repeats)]
  smart = [d.chebyshev( lst[0] ) for lst in smart]
  somes.append(stats.SOME(smart,f"smart,{N}"))

stats.report(somes, 0.01)
