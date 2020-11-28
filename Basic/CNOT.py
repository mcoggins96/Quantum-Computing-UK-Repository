from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, execute,IBMQ

IBMQ.enable_account('Enter API token here')
provider = IBMQ.get_provider(hub='ibm-q')

q = QuantumRegister(2,'q')
c = ClassicalRegister(2,'c')

circuit = QuantumCircuit(q,c)
circuit.x(q[0]) # Pauli x gate applied to first qubit 
circuit.cx(q[0],q[1]) # CNOT applied to both qubits 
circuit.measure(q,c) # Qubits states are measured 

backend = provider.get_backend('ibmq_qasm_simulator') # Specifying qasm simulator as the target device 

print('Provider: ',backend)
print('')

job = execute(circuit, backend, shots=1)
                               
print('Executing Job...')
print('')                   
result = job.result()
counts = result.get_counts(circuit)

print('RESULT: ',counts)
print('')
print('Press any key to close')
input()