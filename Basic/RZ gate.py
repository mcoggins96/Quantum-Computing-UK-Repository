from qiskit import QuantumRegister, ClassicalRegister
from qiskit import QuantumCircuit, execute,IBMQ
from qiskit.tools.monitor import job_monitor
import numpy as np

pi = np.pi

IBMQ.enable_account('ENTER API KEY HERE')
provider = IBMQ.get_provider(hub='ibm-q')

backend = provider.get_backend('ibmq_qasm_simulator')

def rz(rotation):
    circuit = QuantumCircuit(q,c)

    circuit.h(q[0]) # Hadamard gate 
    circuit.rz(rotation,q[0]) # RZ gate
    circuit.h(q[0]) # Hadamard gate 
    circuit.measure(q,c) # Qubit Measurment

    print(circuit)

    job = execute(circuit, backend, shots=8192)
    
    job_monitor(job)
    counts = job.result().get_counts()

    print(counts)
    
q = QuantumRegister(1,'q')
c = ClassicalRegister(1,'c')

rotation = 0
rz(rotation)

rotation = pi/2
rz(rotation)

rotation = pi
rz(rotation)
