from qiskit import QuantumRegister, ClassicalRegister
from qiskit import QuantumCircuit, execute,IBMQ
from qiskit.circuit.library import Permutation
from qiskit.tools.monitor import job_monitor

IBMQ.enable_account('ENTER API Key HERE')
provider = IBMQ.get_provider(hub='ibm-q')

backend = provider.get_backend('ibmq_qasm_simulator')


q = QuantumRegister(8, 'q')
c = ClassicalRegister(8, 'c')

########### PERMUTATION WITH PATTERN 7,0,6,1,5,2,4,3 
circuit = QuantumCircuit(q, c)

circuit.x(q[0])
circuit.x(q[1])
circuit.x(q[2])
circuit.x(q[3])

circuit += Permutation(num_qubits = 8, pattern = [7,0,6,1,5,2,4,3])

circuit.measure(q, c)

job = execute(circuit, backend, shots=100)
job_monitor(job)

counts = job.result().get_counts()

print(circuit)
print(counts)

####### RANDOM PERMUTATION CIRCUIT 
circuit = QuantumCircuit(q, c)

circuit.x(q[0])
circuit.x(q[1])
circuit.x(q[2])
circuit.x(q[3])

circuit += Permutation(num_qubits = 8)

circuit.measure(q, c)

job = execute(circuit, backend, shots=100)
job_monitor(job)

counts = job.result().get_counts()

print(circuit)
print(counts)
