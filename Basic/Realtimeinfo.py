print('\nDevice Monitor')
print('----------------')

from qiskit import IBMQ
from qiskit.tools.monitor import backend_overview

IBMQ.enable_account('Insert API token here') # Insert your API token in to here
provider = IBMQ.get_provider(hub='ibm-q')

backend_overview() # Function to get all information back about each quantum device  

print('\nPress any key to close')
input()