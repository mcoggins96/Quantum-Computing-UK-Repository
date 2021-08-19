from qiskit import QuantumRegister, ClassicalRegister
from qiskit.circuit.library import MCMT
from qiskit import QuantumCircuit, execute,IBMQ
from qiskit.tools.monitor import job_monitor
import numpy as np

IBMQ.enable_account('ENTER API KEY HERE')
provider = IBMQ.get_provider(hub='ibm-q')

backend = provider.get_backend('ibmq_qasm_simulator')

pi = np.pi

q = QuantumRegister(6,'q')
c = ClassicalRegister(2,'c')

circuit = QuantumCircuit(q,c)

#### This circuit shows how to implement a controlled hadamard gate ####
#### consisting of 4 control qubits and 2 target qubits ####

circuit.x(q[0])
circuit.x(q[1])
circuit.x(q[2])
circuit.x(q[3])

circuit += MCMT('h',4,2, label=None)

circuit.measure(q[4],c[0])
circuit.measure(q[5],c[1])

print(circuit)

job = execute(circuit, backend, shots=8192)

job_monitor(job)
counts = job.result().get_counts()

print(counts)
