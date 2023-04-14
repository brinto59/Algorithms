# longest common substring

string1 = "vista"
string2 = "fish"
len1 = len(string1)
len2 = len(string2)

s = []
for i in range(len1+1):
    s.append([0]*(len2+1))

char_tracker = []
for i in range(len1+1):
    char_tracker.append(['']*(len2+1))

substring = ""
maximumChar = 0


for i in range(0, len1):
    for j in range(0, len2):
        if string1[i] == string2[j]:
            s[i+1][j+1] = s[i][j] + 1
            char_tracker[i+1][j+1] = char_tracker[i][j] + string1[i]
            maximumChar = s[i+1][j+1]
            substring = char_tracker[i+1][j+1]
        else:
            s[i+1][j+1] = 0
            char_tracker[i+1][j+1] = ""

print(s)
print(char_tracker)
print(substring, maximumChar)