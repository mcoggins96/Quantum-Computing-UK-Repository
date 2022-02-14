from qiskit import QuantumRegister, ClassicalRegister
from qiskit import QuantumCircuit, execute,IBMQ
from qiskit.tools.monitor import job_monitor
from qiskit.circuit.library import RGQFTMultiplier

IBMQ.enable_account('ENTER API KEY HERE')
provider = IBMQ.get_provider(hub='ibm-q')

backend = provider.get_backend('ibmq_qasm_simulator')

q = QuantumRegister(8,'q')
c = ClassicalRegister(4,'c')

circuit = QuantumCircuit(q,c)

# Operand A = 10 (2)

circuit.x(q[1])

# Operand B = 11 (3)
circuit.x(q[2])
circuit.x(q[3])

circuit1 = RGQFTMultiplier(num_state_qubits=2, num_result_qubits=4)
circuit = circuit.compose(circuit1)

circuit.measure(q[4],c[0])
circuit.measure(q[5],c[1])
circuit.measure(q[6],c[2])
circuit.measure(q[7],c[3])

print(circuit)

job = execute(circuit, backend, shots=2000)
result = job.result()
counts = result.get_counts()
print('2*3')
print('---')
print(counts)



