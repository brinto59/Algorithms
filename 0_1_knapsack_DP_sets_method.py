# 0/1 Knapsack Problem - Dynamic Programming
# sets method
def merge(set0: list, set1: list, m) -> list:
    result = []
    i = 0
    j = 0
    k = 0
    len0 = len(set0)
    len1 = len(set1)
    while i < len0 and j < len1:
        if set0[i][0] <= set1[j][0]:
            if not(set0[i][0] == set1[j][0] and set0[i][1] == set1[j][1]) and set0[i][1] < set1[j][1] and set0[i][1] <= m:
                result.append(set0[i])
            i += 1
        else:
            if not(set0[i][0] == set1[j][0] and set0[i][1] == set1[j][1]) and set1[j][1] < set1[i][1] and set1[j][1] <= m:
                result.append(set1[j])
            j += 1
    while i < len0:
        if set0[i][1] <= m:
            result.append(set0[i])
        i += 1
    while j < len1:
        if set1[j][1] <= m:
            result.append(set1[j])
        j += 1

    return result


def solution(s, x, p, wt, n, m):
    k = len(s[n]) - 1
    search = s[n][k]
    for i in range(n, 0, -1):
        if search in s[i-1]:
            x[i] = 0
        else:
            x[i] = 1
            search = [search[0] - p[i], search[1] - wt[i]]


def main():
    n = 4
    m = 8
    p = [0, 5, 1, 6, 2]
    wt = [0, 4, 2, 5, 3]
    s = [[[0, 0]], [], [], [], []]  # sets 0, 1, 2, 3, 4
    x = [-1] * 5
    for i in range(1, n + 1):
        for j in range(len(s[i-1])):
            s[i].append([s[i-1][j][0] + p[i], s[i-1][j][1] + wt[i]])
        s[i] = merge(s[i-1], s[i], m)
    # print(s[0])
    # print(s[1])
    # print(s[2])
    # print(s[3])
    # print(s[4])

    solution(s, x, p, wt, n, m)
    print(s[4])
    print(x)


if __name__ == "__main__":
    main()






