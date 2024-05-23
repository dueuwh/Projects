import numpy as np
import matplotlib.pyplot as plt
import copy as c

def Determinant(input_matrix):
    return 0

# An adapter should be built for each function of the solver
def Linear_Independant_Test(solver, test_matrix):
    output = solver(test_matrix)
    # adapter start

    # adapter end
    if test_matrix.shape[0] == output:
        return True
    else:
        return False


def projection(vector_u: np.ndarray, vector_a: np.ndarray) -> np.ndarray:
    return (np.dot(vector_u, vector_a)/np.dot(vector_u, vector_u))*vector_u


def Gram_Schmidt_Process(input_matrix, error):
    matrix_q = np.empty(input_matrix.shape)
    matrix_q[:, 0] = input_matrix[:, 0]/np.linalg.norm(input_matrix[:, 0], 2)
    for i in range(input_matrix.shape[1]-1):
        temp = input_matrix[:, i+1].astype(float)

        for j in range(i+1):
            temp -= projection(matrix_q[:, j], input_matrix[:, i+1])
        temp = temp/np.linalg.norm(temp, 2)
        matrix_q[:, i+1] = temp
    output = np.dot(matrix_q.T, input_matrix)
    for i in range(output.shape[0]):
        for j in range(output.shape[1]):
            if abs(output[i, j]) < error:
                output[i, j] = 0
    return output

def Sylvester_Criterion(input_matrix):
    return 0

def Householder_Reflections(input_matrix):
    output = "Implementation in progress..."
    raise ValueError(output)

def Number_Theoretic_Transform(input_matrix):
    return 0

if __name__ == "__main__":
    a_qr = np.array([[12, 6, -4], [-51, 167, 24], [4, -68, -41]]).T  # test matrix for QR decomposition
    print(f"a_qr:\n{a_qr}\n")
    error = 1e-10
    qr_result = Gram_Schmidt_Process(a_qr, error)

    print(qr_result)

