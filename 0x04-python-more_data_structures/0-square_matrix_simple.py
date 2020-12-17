#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    mtx = [[]]
    mtx = [[element ** 2 for element in matrix[i]] for i in range(len(matrix))]
    return mtx
            
