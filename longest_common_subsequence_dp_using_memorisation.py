# Longest Common Subsequence - Dynamic Programming
# using Memorisation Method
string1 = "stone"
string2 = "longest"
len1 = len(string1)
len2 = len(string2)
c = []
for i in range(len1+1):
    c.append([0]*(len2+1))


def lcs(i, j):
    if i == len1 or j == len2:
        return 0
    elif string1[i] == string2[j]:
        if c[i+1][j+1] != 0:
            return 1 + c[i+1][j+1]
        else:
            c[i+1][j+1] = lcs(i+1, j+1)
            return 1 + c[i+1][j+1]
    else:
        if c[i+1][j] == 0:
            c[i+1][j] = lcs(i+1, j)
        if c[i][j+1] == 0:
            c[i][j+1] = lcs(i, j+1)
        return max(c[i+1][j], c[i][j+1])


print(lcs(0, 0))
