print('\n Quantum Toffoli Program')
print('--------------------------')
print('Programmed by Macauley Coggins for Quantum Computing UK\n')

from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, execute,IBMQ

IBMQ.enable_account('Enter API key here')
provider = IBMQ.get_provider(hub='ibm-q')

q = QuantumRegister(3,'q')
c = ClassicalRegister(3,'c')

circuit = QuantumCircuit(q,c)
circuit.x(q[0])
circuit.x(q[1])
circuit.ccx(q[0],q[1],q[2])
circuit.measure(q,c)

backend = provider.get_backend('ibmq_qasm_simulator')

print('Provider: ',backend)

job = execute(circuit, backend, shots=1024)
                               
print('Executing Job...\n')                  
result = job.result()
counts = result.get_counts(circuit)

print('RESULT: ',counts,'\n')
print('Press any key to close')
input()