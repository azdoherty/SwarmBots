import numpy as np

P = np.array(np.identity(4)) * 100
jacobian = np.array([[1.0, 0.0, 1.0, 0.0],
                             [0.0, 1.0,  0.0, 1.0],
                             [0.0, 0.0, 1.0, 0.0],
                             [0.0, 0.0, 0.0, 1.0]])

print (np.dot(P, jacobian.transpose()))