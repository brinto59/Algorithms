# Reliability Design - Dynamic Programming
import math


def merge(set0: list, set1: list, m) -> list:
    # print("set0", set0)
    # print("set1", set1)
    result = []
    i = 0
    j = 0
    len0 = len(set0)
    len1 = len(set1)
    while i < len0 and j < len1:
        if set0[i][0] <= set1[j][0]:

            if not(set0[i][0] == set1[j][0] and set0[i][1] == set1[j][1]) and set0[i][1] < set1[j][1] and set0[i][1] <= m:
                result.append(set0[i])
            i += 1
        else:

            if not(set0[i][0] == set1[j][0] and set0[i][1] == set1[j][1]) and set1[j][1] < set0[i][1] and set1[j][1] <= m:
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


def find_solution(s, u, solution):
    length_of_s = len(s)
    length_of_last_list = len(s[length_of_s-1][0])
    k = s[length_of_s-1][0][length_of_last_list-1]
    for i in range(length_of_s-2, -1, -1):
        for j in range(0, u[i+1]):
            if k in s[i][1][j]:
                index = s[i][1][j].index(k)
                solution[i] = j+1
                k = s[i][0][index]


def main():
    n = 3
    mc = 105  # maximum cost
    c = [0, 30, 15, 20]
    r = [0, 0.9, 0.8, 0.5]
    u = [0]
    tc = 0  # total cost of buying one thing of each

    s = [
        [[[1, 0]], []],   # (r, c)  # first list - after merging, second list - before merging
        [[], []],
        [[], []],
        [[]],
    ]

    solution = [0] * n  # D1, D2, D3

    for i in range(1, n+1):
        tc += c[i]

    remaining = mc - tc
    for j in range(1, n+1):
        u.append(math.floor(remaining/c[j])+1)

    for i in range(0, n):
        for j in range(1, u[i+1]+1):
            reliability = 1 - (1 - r[i+1])**j
            s[i][1].append([])
            for k in range(0, len(s[i][0])):
                s[i][1][j-1].append([s[i][0][k][0]*reliability, s[i][0][k][1] + j * c[i+1]])
            # print(s)
            s[i+1][0] = merge(s[i+1][0], s[i][1][j-1], mc)
        print(s[i+1][0])

    find_solution(s, u, solution)
    print(solution)


if __name__ == "__main__":
    main()
