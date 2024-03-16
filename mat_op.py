import ran_strrr as ran
import matrix_value_add as m
import numpy as np
def mat_add(matrix1,matrix2):
    rows1, cols1 = len(matrix1), len(matrix1[0])
    

    result_matrix = [[0] * cols1 for _ in range(rows1)]
    for i in range(rows1):
        for j in range(cols1):
            result_matrix[i][j] = matrix1[i][j] + matrix2[i][j]
    return result_matrix,matrix2
def mat_sub(matrix1,matrix2):
    rows1, cols1 = len(matrix1), len(matrix1[0])
    result_matrix = [[0] * cols1 for _ in range(rows1)]
    for i in range(rows1):
        for j in range(cols1):
            result_matrix[i][j] = matrix1[i][j] - matrix2[i][j]
    return result_matrix,matrix2
def mat_multiply(matrix1, matrix2):
    rows1, cols1 = len(matrix1), len(matrix1[0])
    rows2, cols2 = len(matrix2), len(matrix2[0])

    # Check if matrices can be multiplied
    if cols1 != rows2:
        print("Matrices cannot be multiplied due to incompatible dimensions.")
        return None

    # Initialize the result matrix with zeros
    result_matrix = [[0] * cols2 for _ in range(rows1)]

    # Perform matrix multiplication
    for i in range(rows1):
        for j in range(cols2):
            if matrix2[i][j]!=0:
                result_matrix[i][j] += matrix1[i][j] * matrix2[i][j]
            else:
                result_matrix[i][j]+=matrix1[i][j]

    return result_matrix,matrix2


def mat_divide(matrix1, matrix2):
    rows1, cols1 = len(matrix1), len(matrix1[0])
    rows2, cols2 = len(matrix2), len(matrix2[0])

    # Check if matrices can be multiplied
    if cols1 != rows2:
        print("Matrices cannot be multiplied due to incompatible dimensions.")
        return None

    # Initialize the result matrix with zeros
    result_matrix = [[0] * cols2 for _ in range(rows1)]

    # Perform matrix division
    for i in range(rows1):
        for j in range(cols2):
            # Check if denominator is not zero
            if matrix2[i][j] != 0:
                result_matrix[i][j] = int(matrix1[i][j] / matrix2[i][j])
            else:
                result_matrix[i][j] = int(matrix1[i][j])
    return result_matrix, matrix2

def transpose(matrix,m):
    transposed_matrix = np.transpose(matrix)
    return transposed_matrix.tolist(),m


