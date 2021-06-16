from qiskit import QuantumRegister, ClassicalRegister
from qiskit import QuantumCircuit, execute,IBMQ
from qiskit.tools.monitor import job_monitor

IBMQ.enable_account('Enter API key here')
provider = IBMQ.get_provider(hub='ibm-q')

backend = provider.get_backend('ibmq_qasm_simulator')


q = QuantumRegister(8, 'q')
c = ClassicalRegister(1, 'c')

circuit = QuantumCircuit(q, c)

circuit.x(q[0])
circuit.x(q[1])
circuit.x(q[2])
circuit.x(q[3])

circuit.ccx(q[0], q[1], q[4])
circuit.ccx(q[2], q[4], q[5])
circuit.ccx(q[3], q[5], q[6])

circuit.cx(q[6], q[7]) 

circuit.ccx(q[3], q[5], q[6])
circuit.ccx(q[2], q[4], q[5])
circuit.ccx(q[0], q[1], q[4])

circuit.measure(q[7], c[0])

job = execute(circuit, backend, shots=100)
job_monitor(job)

counts = job.result().get_counts()

print(circuit)
print(counts)
