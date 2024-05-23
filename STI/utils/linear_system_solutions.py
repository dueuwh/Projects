import numpy as np
import typing as t
from basic_tools import *
from linear_system_solution_params import LSS_PARAMS as lss_params

# not for general purpose, only for interpolation for data like:
# [[x_1, y_1], [x_2, y_2], ..., [x_n, y_n]]
def Gauss_Jordan_Elimination(input_list: list[t.Union[list, tuple]], order) -> list:

    # matrix initialization
    output = np.empty((order, order+1))
    if len(input_list) < order:
        raise ValueError(f"size of input_list is shorter than the order: list size: {len(input_list)}, order: {order}")

    for i in range(order):
        for j in range(order):
            output[i, j] = input_list[i][0]**j
        output[i, j+1] = input_list[i][1]

    # forward
    for i in range(order):
        if output[i, i] != 1.0:
            output[i, :] = output[i, :]/output[i, i]
        for j in range(order-i-1):
            output[i+j+1, :] = output[i+j+1, :] - output[i, :]*output[i+j+1, i]
    # backward
    for i in range(order-1):
        for j in range(order-i-1):
            output[order-1-1-i-j, :] = output[order-1-1-i-j, :] - output[order-1-i, :]*output[order-1-1-i-j, order-1-i]
    return output

def QR_decomposition(input_matrix):
    if lss_params.QR_decomposition['method'] == "Gram_Schmidt_Process":
        return Gram_Schmidt_Process(input_matrix, lss_params.QR_decomposition['error'])
    elif lss_params.QR_decomposition['method'] == "Householder_Reflections":
        return Householder_Reflections(input_matrix)

def SVD_decomposition():
    return 0

def LU_decomposition():
    return 0

def Convex_Optimization():
    return 0

def Tridiagonal_matrix_algorithm(input_matrix):

    return 0

def Gauss_Seidel_method():
    return 0

def Laplace_Transform():
    return 0

def Legendre_Polynomial():
    return 0

def Chebyshev_Polynomial():
    return 0

def Least_Squares_Method():
    return 0

def Newton_Method():
    return 0

def Genetic_Algorithm():
    return 0

def Cholesky_Factorization(input_matrix):
    row, col = input_matrix.shape()
    if row != col:
        raise ValueError(f"The row({row}) and col({col}) are not same.\nThe input matrix should be a square matrix")

    semi_positive_definite = Sylvester_Criterion(input_matrix)
    if semi_positive_definite == False:
        raise ValueError(f"The input matrix does not satisfy semi-positive definiteness\n * Use other method")



if __name__ == "__main__":
    a = [[1,2], [3,4], [5,6], [7,8], [9,10]]
    order = 4
    result = Gauss_Jordan_Elimination(input_list=a, order=order)

    a_qr = np.array([[12, 6, -4], [-51, 167, 24], [4, -68, -41]]).T  # test matrix for QR decomposition
    print(f"a_qr:\n{a_qr}\n")
    error = 1e-10
    qr_result = Gram_Schmidt_Process(a_qr, error)

    print(qr_result)



