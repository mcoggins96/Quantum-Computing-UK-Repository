import neal
sampler = neal.SimulatedAnnealingSampler()
#AND GATE
print("AND GATE")
e = -2
d = -2
h = {'a': d, 'b': e, 'out':1}
J = {('a', 'out'): -1,('b','out'):-1}
response = sampler.sample_ising(h, J)
print(response)
#NAND GATE
print("NAND GATE")
e = -2
d = -2
h = {'a': d, 'b': e, 'out':-1}
J = {('a', 'out'): 1,('b','out'):1}
response = sampler.sample_ising(h, J)
print(response)