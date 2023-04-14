# Longest Common Subsequence - Dynamic Programming
# using recursion
string1 = "bd"
string2 = "abcd"
len1 = len(string1)
len2 = len(string2)


def lcs(i, j):
    if i == len1 or j == len2:
        return 0
    elif string1[i] == string2[j]:
        return 1 + lcs(i+1, j+1)
    else:
        return max(lcs(i+1, j), lcs(i, j+1))


print(lcs(0, 0))