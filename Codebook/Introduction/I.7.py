# I.7: Universal gate sets 

import pennylane as qml
from pennylane import numpy as np
dev = qml.device("default.qubit", wires=1)

##################
# YOUR CODE HERE #
##################

# ADJUST THE VALUES OF PHI, THETA, AND OMEGA
phi, theta, omega =np.pi/2,np.pi/2, np.pi/2

@qml.qnode(dev)
def hadamard_with_rz_rx():
    qml.RZ(phi, wires=0) # RZ hepls adjust the global phase, complex number 
    qml.RX(theta, wires=0)  # RX (theta/2)!! = RX(pi/4)
    qml.RZ(omega, wires=0)
    return qml.state()


dev = qml.device("default.qubit", wires=1)

@qml.qnode(dev)
def convert_to_rz_rx():
    ##################
    # YOUR CODE HERE #
    ##################

    # IMPLEMENT THE CIRCUIT IN THE PICTURE USING ONLY RZ AND RX
    qml.RZ(np.pi/2, wires=0)
    qml.RX(np.pi/2, wires=0)
    qml.RZ(np.pi/2, wires=0)
    
    qml.RZ(np.pi/4, wires=0)

    qml.RZ(np.pi,wires=0)   # important: Y=iXZ = i RX(pi) RZ(pi) 
    qml.RX(np.pi,wires=0)
    


    return qml.state()



# this one is a horrible question, I don't know how to do it, I just guess here!
dev = qml.device("default.qubit", wires=1)

@qml.qnode(dev)
def unitary_with_h_and_t():
    ##################
    # YOUR CODE HERE #
    ##################
    
    # APPLY ONLY H AND T TO PRODUCE A CIRCUIT THAT EFFECTS THE GIVEN MATRIX
    qml.Hadamard(wires=0)
    qml.T(wires=0)
    qml.Hadamard(wires=0)
    qml.T(wires=0)
    qml.T(wires=0)
    qml.Hadamard(wires=0)





    return qml.state()

# HTHTTH
# HTTHTH