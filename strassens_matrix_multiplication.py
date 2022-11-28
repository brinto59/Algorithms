# Strassen's matrix multiplication
import sys


def check(matrix_a, matrix_b):
    length_a_row = len(matrix_a)
    length_a_col = len(matrix_a[0])
    length_b_row = len(matrix_b)
    length_b_col = len(matrix_b[0])
    if length_a_col != length_b_row:
        sys.exit("matrix multiplication can not be done")

    maximum_num = length_a_row if length_a_row > length_b_col else length_b_col
    power = 1
    while 2**power < maximum_num:
        power += 1
    matrix_a = fill_out_with_zeros(matrix_a, power)
    matrix_b = fill_out_with_zeros(matrix_b, power)
    return [matrix_a, matrix_b, power, length_a_row, length_b_col]


def fill_out_with_zeros(matrix, pwr):
    for i in range(2**pwr):
        for j in range(2**pwr):
            if len(matrix[i]) < 2**pwr:
                matrix[i].append(0)
        if len(matrix) < 2**pwr:
            matrix.append([])
    return matrix


def addition_subtraction(matrix_a, matrix_b, sign, power):
    matrix_c = []
    if sign == "+" or sign == "-":
        for i in range(2**power):
            matrix_c.append([])
            for j in range(2**power):
                matrix_c[i].append(eval(f"{matrix_a[i][j]} {sign} {matrix_b[i][j]}"))
    else:
        sys.exit("sign is not either plus or minus")
    return matrix_c


def matrix_multiplication(matrix_a, matrix_b, power):
    if 2**power <= 2:
        result_matrix = [[], []]
        result_matrix[0].append(matrix_a[0][0] * matrix_b[0][0] + matrix_a[0][1] * matrix_b[1][0])
        result_matrix[0].append(matrix_a[0][0] * matrix_b[0][1] + matrix_a[0][1] * matrix_b[1][1])
        result_matrix[1].append(matrix_a[1][0] * matrix_b[0][0] + matrix_a[1][1] * matrix_b[1][0])
        result_matrix[1].append(matrix_a[1][0] * matrix_b[0][1] + matrix_a[1][1] * matrix_b[1][1])
        return result_matrix
    else:
        n = 2**power
        mid = int(n/2)
        a11 = divide_matrix(matrix_a, [0, 0], [mid, mid])
        a12 = divide_matrix(matrix_a, [0, mid], [mid, n])
        a21 = divide_matrix(matrix_a, [mid, 0], [n, mid])
        a22 = divide_matrix(matrix_a, [mid, mid], [n, n])
        b11 = divide_matrix(matrix_b, [0, 0], [mid, mid])
        b12 = divide_matrix(matrix_b, [0, mid], [mid, n])
        b21 = divide_matrix(matrix_b, [mid, 0], [n, mid])
        b22 = divide_matrix(matrix_b, [mid, mid], [n, n])
        # strassen's formula
        p = matrix_multiplication(addition_subtraction(a11, a22, "+", power-1), addition_subtraction(b11, b22, "+", power-1), power-1)
        q = matrix_multiplication(addition_subtraction(a21, a22, "+", power-1), b11, power-1)
        r = matrix_multiplication(a11, addition_subtraction(b12, b22, "-", power-1), power-1)
        s = matrix_multiplication(a22, addition_subtraction(b21, b11, "-", power-1), power-1)
        t = matrix_multiplication(addition_subtraction(a11, a12, "+", power-1), b22, power-1)
        u = matrix_multiplication(addition_subtraction(a21, a11, "-", power-1), addition_subtraction(b11, b12, "+", power-1), power-1)
        v = matrix_multiplication(addition_subtraction(a12, a22, "-", power-1), addition_subtraction(b21, b22, "+", power-1), power-1)

        c11 = addition_subtraction(addition_subtraction(p, s, "+", power-1), addition_subtraction(t, v, "-", power-1), "-", power-1)
        c12 = addition_subtraction(r, t, "+", power-1)
        c21 = addition_subtraction(q, s, "+", power-1)
        c22 = addition_subtraction(addition_subtraction(p, r, "+", power-1), addition_subtraction(q, u, "-", power-1), "-", power-1)
        c = []
        k = 0

        for j in range(2):
            c.append([])
            c[k].extend([*c11[j], *c12[j]])
            k += 1
        for j in range(2):
            c.append([])
            c[k].extend([*c21[j], *c22[j]])
            k += 1
        return c


def divide_matrix(matrix, starting, ending):  # starting = [row, col] , ending = [row, col]
    result_matrix = []
    k = 0
    for i in range(starting[0], ending[0]):
        result_matrix.append([])
        for j in range(starting[1], ending[1]):
            result_matrix[k].append(matrix[i][j])
        k += 1
    return result_matrix


def main():
    matrix_a = [[2, 1], [3, 4]]
    matrix_b = [[2, 1, 3], [4, 5, 6]]
    matrix_a, matrix_b, power, length_a_row, length_b_col = check(matrix_a, matrix_b)
    print(divide_matrix(matrix_multiplication(matrix_a, matrix_b, power), [0, 0], [length_a_row, length_b_col]))


if __name__ == "__main__":
    main()



