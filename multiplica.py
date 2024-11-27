import random
import time

n = 2048

#populate the matrices with random values between 0.0 and 1.0
A = [[random.random() for row in range(n)] for col in range(n)]
B = [[random.random() for row in range(n)] for col in range(n)]
C = [[0 for row in range(n)] for col in range(n)]

start = time.time()
#matrix multiplication
for i in range(n):
    for j in range(n):
        for k in range(n):
            C[i][j] += A[i][k] * B[k][j]

end = time.time()
print("Elapsed time in seconds %0.6f" % (end-start))
