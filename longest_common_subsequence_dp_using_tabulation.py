# Longest Common Subsequence - Dynamic Programming
# using Tabulation Method
string1 = "stone"
string2 = "longest"
len1 = len(string1)
len2 = len(string2)

char_tracker = []
for i in range(len1+1):
    char_tracker.append(['']*(len2+1))

lcs = []
for i in range(len1+1):
    lcs.append([0]*(len2+1))


for i in range(0, len2):
    for j in range(0, len1):
        if string1[j] == string2[i]:
            lcs[j+1][i+1] = lcs[j][i] + 1
            char_tracker[j+1][i+1] = char_tracker[j][i] + string1[j]
        else:
            lcs[j+1][i+1] = max(lcs[j][i+1], lcs[j+1][i])
            char_tracker[j+1][i+1] = char_tracker[j][i+1] if len(char_tracker[j][i+1]) > len(char_tracker[j+1][i]) else char_tracker[j+1][i]


print(lcs[len1][len2])
print(char_tracker[len1][len2])