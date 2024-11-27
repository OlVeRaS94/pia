import numpy as np
import time


TAM=2048

#matriu = [[np.random.rand() for j in range(TAM)] for i in range(TAM)]

m1 = np.random.rand(TAM,TAM)
m2 = np.random.rand(TAM,TAM)
desti = np.zeros((TAM,TAM),dtype=float)

start = time.time()
nova=np.dot(m1,m2)
end = time.time()
print("Amb np: Elapsed time in seconds %0.6f" % (end-start))


start = time.time()
#matrix multiplication
for i in range(TAM):
    for j in range(TAM):
        for k in range(TAM):
            desti[i][j] += m1[i][k] * m2[k][j]
end = time.time()
print("Sense np: Elapsed time in seconds %0.6f" % (end-start))