# Optimal Binary Search Tree
# Successful and Unsuccessful Probability

import sys

n = 4
keys = [10, 20, 30, 40]  # have to be ordered
p = [0, 3, 3, 1, 1]
q = [2, 3, 1, 1, 1]
# cost
c = [
    [0]*5,
    [0]*5,
    [0]*5,
    [0]*5,
    [0]*5,
    [0]*5
]

w = [
    [0]*5,
    [0]*5,
    [0]*5,
    [0]*5,
    [0]*5
]
for i in range(1, n+1):
    w[i][i-1] = q[i-1]

# Root
R = [
    [0] * 5,
    [0] * 5,
    [0] * 5,
    [0] * 5,
    [0] * 5
]

for j in range(0, n):
    for i in range(1, n-j+1):
        minimum = sys.maxsize
        w[i][i+j] = w[i][i+j-1] + p[i+j] + q[i+j]
        for k in range(i, i+j+1):
            if c[i][k-1] + c[k+1][i+j] < minimum:
                minimum = c[i][k-1] + c[k+1][i+j]
                R[i][i+j] = k
        c[i][i+j] = minimum + w[i][i+j]


def find_binary_tree(i, j, k):
    if n + 1 > i >= 0 and 0 <= j < n+1 and R[i][j] != 0:
        key = R[i][j]
        bt[k] = keys[key-1]
        find_binary_tree(i, key-1, 2*k)
        find_binary_tree(key+1, j, 2*k+1)


i = 1
j = 4
bt = [0] * (2*4+2)
k = 1
find_binary_tree(i, j, k)
print("optimal binary tree: ", bt)


# display
# cost
print("Cost")
for i in range(1, n+1):
    for j in range(1, n+1):
        print(c[i][j], end=" ")
    print("")

# w
print("w")
for i in range(1, n+1):
    for j in range(0, n+1):
        print(w[i][j], end=" ")
    print("")

# root
print("Root")
for i in range(1, n+1):
    for j in range(1, n+1):
        print(R[i][j], end=" ")
    print("")
