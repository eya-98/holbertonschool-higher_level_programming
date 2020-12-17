#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    mtx = [[]]
    for i in range(len(matrix)):
        mtx = [element ** 2 for element in matrix[i]]
    return mtx
            
