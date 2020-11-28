import numpy as np
from qiskit import BasicAer
from qiskit.aqua import QuantumInstance, aqua_globals
from qiskit.aqua.components.feature_maps import SecondOrderExpansion
from qiskit.aqua.components.multiclass_extensions import (ErrorCorrectingCode,AllPairs,OneAgainstRest)
from qiskit.aqua.algorithms import QSVM
from qiskit.aqua.utils import get_feature_dimension
from qiskit import IBMQ

print('Quantum SVM')
print('-----------\n')

shots = 8192 # Number of times the job will be run on the quantum device 

training_data = {'A': np.asarray([[0.324],[0.565],[0.231],[0.756],[0.324],[0.534],[0.132],[0.344]]),'B': np.asarray([[1.324],[1.565],[1.231],[1.756],[1.324],[1.534],[1.132],[1.344]])}
testing_data = {'A': np.asarray([[0.024],[0.456],[0.065],[0.044],[0.324]]),'B': np.asarray([[1.777],[1.341],[1.514],[1.204],[1.135]])}

IBMQ.enable_account('ENTER API KEY HERE')
provider = IBMQ.get_provider(hub='ibm-q')

backend = provider.get_backend('ibmq_qasm_simulator') # Specifying Quantum device

num_qubits = 1

feature_map = SecondOrderExpansion(feature_dimension=num_qubits,depth=2,entanglement='full')

svm = QSVM(feature_map, training_data,testing_data) # Creation of QSVM

quantum_instance = QuantumInstance(backend,shots=shots,skip_qobj_validation=False)

print('Running....\n')

result = svm.run(quantum_instance) # Running the QSVM and getting the accuracy

data = np.array([[1.453],[1.023],[0.135],[0.266]]) #Unlabelled data

prediction = svm.predict(data,quantum_instance) # Predict using unlabelled data 

print('Prediction of Smoker or Non-Smoker based upon gene expression of CDKN2A\n')
print('Accuracy: ' , result['testing_accuracy'],'\n')
print('Prediction from input data where 0 = Non-Smoker and 1 = Smoker\n')
print(prediction)



