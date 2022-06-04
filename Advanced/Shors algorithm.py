from qiskit import IBMQ
from qiskit.utils import QuantumInstance
from qiskit.algorithms import Shor


IBMQ.enable_account('ENTER API KEY HERE') # Enter your API token here
provider = IBMQ.get_provider(hub='ibm-q')

backend = provider.get_backend('ibmq_qasm_simulator') # Specifies the quantum device

print('\n Shors Algorithm')
print('--------------------')
print('\nExecuting...\n')

factors = Shor(QuantumInstance(backend, shots=100, skip_qobj_validation=False)) 

result_dict = factors.factor(N=21, a=2)
result = result_dict.factors

print(result)
print('\nPress any key to close')
input()
