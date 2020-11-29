print('\n Superdense Coding')
print('--------------------------\n')

from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, execute,IBMQ
from qiskit.tools.monitor import job_monitor

IBMQ.enable_account('ENTER API TOKEN')
provider = IBMQ.get_provider(hub='ibm-q')

q = QuantumRegister(2,'q')
c = ClassicalRegister(2,'c')

backend = provider.get_backend('ibmq_qasm_simulator')
print('Provider: ',backend)

#################### 00 ###########################
circuit = QuantumCircuit(q,c) 

circuit.h(q[0]) # Hadamard gate applied to q0
circuit.cx(q[0],q[1]) # CNOT gate applied
circuit.cx(q[0],q[1]) 
circuit.h(q[0])  

circuit.measure(q,c) # Qubits measured    

job = execute(circuit, backend, shots=10)
                               
print('Executing Job...\n')               
job_monitor(job)
counts = job.result().get_counts()

print('RESULT: ',counts,'\n')

#################### 10 ###########################
circuit = QuantumCircuit(q,c) 

circuit.h(q[0])
circuit.cx(q[0],q[1])
circuit.x(q[0]) # X-gate applied
circuit.cx(q[0],q[1])
circuit.h(q[0])

circuit.measure(q,c)
       
job = execute(circuit, backend, shots=10)
                               
print('Executing Job...\n')                  
job_monitor(job)
counts = job.result().get_counts()

print('RESULT: ',counts,'\n')

#################### 01 ###########################
circuit = QuantumCircuit(q,c) 

circuit.h(q[0])
circuit.cx(q[0],q[1])
circuit.z(q[0]) # Z-gate applied to q0 
circuit.cx(q[0],q[1])
circuit.h(q[0])

circuit.measure(q,c)
      
job = execute(circuit, backend, shots=10)
                               
print('Executing Job...\n')               
job_monitor(job)
counts = job.result().get_counts()

print('RESULT: ',counts,'\n')

#################### 11 ###########################
circuit = QuantumCircuit(q,c) 

circuit.h(q[0])
circuit.cx(q[0],q[1])
circuit.z(q[0]) # Z-gate applied 
circuit.x(q[0]) # X-gate applied 
circuit.cx(q[0],q[1])
circuit.h(q[0])

circuit.measure(q,c)

job = execute(circuit, backend, shots=10)
                               
print('Executing Job...\n')               
job_monitor(job)
counts = job.result().get_counts()

print('RESULT: ',counts,'\n')
print('Press any key to close')
input()