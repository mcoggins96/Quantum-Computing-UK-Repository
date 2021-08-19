from qiskit import QuantumRegister, ClassicalRegister
from qiskit import QuantumCircuit, execute,IBMQ
from qiskit.tools.monitor import job_monitor
from qiskit.circuit.library import Diagonal
import numpy as np

pi = np.pi

IBMQ.enable_account('ENTER API KEY HERE')
provider = IBMQ.get_provider(hub='ibm-q')

backend = provider.get_backend('ibmq_qasm_simulator')

diagonals = [-1,-1,-1,-1]

q = QuantumRegister(2,'q')
c = ClassicalRegister(2,'c')

circuit = QuantumCircuit(q,c)

circuit.h(q[0])
circuit.h(q[1])
circuit += Diagonal(diagonals)
circuit.h(q[0])
circuit.h(q[1])


circuit.measure(q,c) # Qubit Measurment

print(circuit)

job = execute(circuit, backend, shots=8192)
    
job_monitor(job)
counts = job.result().get_counts()

print(counts)
    
