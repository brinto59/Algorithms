# Matrix Chain Multiplication
import sys

n = 5
p = [5, 4, 6, 2, 7]
m = [[0]*5,
     [0]*5,
     [0]*5,
     [0]*5,
     [0]*5
     ]
s = [[0]*5,
     [0]*5,
     [0]*5,
     [0]*5,
     [0]*5
     ]

minimum = 0

for i in range(1, n-1):
    for j in range(1, n-i):
        minimum = sys.maxsize
        for k in range(j, j+i):
            q = m[j][k] + m[k+1][j+i] + p[j-1] * p[k] * p[j+i]
            if q < minimum:
                minimum = q
                s[j][i+j] = k
        m[j][i+j] = minimum


print(m[1][n-1])
print(s)

