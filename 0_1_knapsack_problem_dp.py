# 0/1 Knapsack Problem - Dynamic Programming
# tabular method

n = 4
m = 8
p = [0, 1, 2, 5, 6]
wt = [0, 2, 3, 4, 5]
v = [
    [0] * 9, [0] * 9, [0] * 9, [0] * 9, [0] * 9
]
x = [-1] * 5

for i in range(1, n+1):
    for j in range(m+1):
        if j == 0:
            v[i][j] = 0
        elif wt[i] <= j:
            v[i][j] = max(p[i] + v[i-1][j-wt[i]], v[i-1][j])
        else:
            v[i][j] = v[i-1][j]

print(v)


j = m
while i > 0 and j >= 0:
    if v[i][j] == v[i-1][j]:
        x[i] = 0
        i -= 1
    else:
        x[i] = 1
        j = j - wt[i]
        i -= 1

print(x)
