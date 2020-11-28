from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, execute, IBMQ

IBMQ.enable_account('Insert account token here') # Get this from your IBM Q account

provider = IBMQ.get_provider(hub='ibm-q')

q = QuantumRegister(1,'q') # Initialise quantum register
c = ClassicalRegister(1,'c') # Initialise classical register

circuit = QuantumCircuit(q,c) # Initialise circuit
circuit.h(q[0]) # Put Qubit 0 in to superposition using hadamard gate 
circuit.measure(q,c) # Measure qubit

backend = provider.get_backend('ibmq_qasm_simulator') # Set device to IBMs quantum simulator
job = execute(circuit, backend, shots=1024) # Execute job and run program 1024 times 
            
result = job.result() # Get result
counts = result.get_counts(circuit) # Count the number of measurements for each state
print('RESULT: ',counts) # Print result 
print('Press any key to close')
input()