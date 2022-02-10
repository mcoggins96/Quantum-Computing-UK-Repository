from qiskit import QuantumRegister, ClassicalRegister
from qiskit import QuantumCircuit, execute,IBMQ
from qiskit.tools.monitor import job_monitor
import numpy
import matplotlib.pyplot as plt

pi = numpy.pi

IBMQ.enable_account('ENTER API KEY HERE')
provider = IBMQ.get_provider(hub='ibm-q')

backend = provider.get_backend('ibmq_armonk')

q = QuantumRegister(1,'q')
c = ClassicalRegister(1,'c')

phi = 0

a = []
b = []

xticks = []
qc_list = []

while phi <= 2*pi:  

    xticks.append(phi)
    
    circuit = QuantumCircuit(q,c)
    circuit.rx(phi,q[0]) #RX gate where Phi is the rotation angle
    circuit.measure(q,c) # Qubit Measurement

    qc_list.append(circuit)

    phi += pi/8
    
job = execute(qc_list, backend, shots=8192)
    
job_monitor(job)
counts = job.result().get_counts()

highest_count1 = 0
highest_count1_1 = 0
highest_count1_0 = 0
index1 = 0

highest_count0 = 0
highest_count0_1 = 0
highest_count0_0 = 0
index0 = 0

for count in counts:
    a.append(count['0'])
    b.append(count['1'])

    if count['1'] > highest_count1:
        highest_count1 = count['1']
        index1 = counts.index(count)
        highest_count1_1 = count['1']
        highest_count1_0 = count['0']

    if count['0'] > highest_count0:
        highest_count0 = count['0']
        index0 = counts.index(count)
        highest_count0_1 = count['1']
        highest_count0_0 = count['0']
   

print("\nOptimal rotation angle for '1' is: ", xticks[index1], ", Counts: 0:", highest_count1_0,  "1:", highest_count1_1)
print("Optimal rotation angle for '0' is: ", xticks[index0], ", Counts: 0:", highest_count0_0,  "1:", highest_count0_1)

plt.suptitle('Rabi Oscillations on IBMQ Armonk')
plt.plot(xticks,a)
plt.plot(xticks,b)
plt.legend(["Measurements for '0' ", "Measurements for '1'"])
plt.show()