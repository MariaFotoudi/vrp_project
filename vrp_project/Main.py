from Solver2 import *

m = model()
m.BuildModel()
s = Solver2(m)
sol = s.solve()