"""
There is a board (matrix). Every cell of the board contains one integer, which is 0 initially.

SetRow i x: changes all values in the cells on row "i" to value "x"
SetCol j x: changes all values in the cells on column "i" to value "x"
QueryRow i: output the sum of values on row "i"
QueryCol j: output the sum of values on column j


Board's dimensions are 256 * 256
"""

def queryBoard(query, n, x):
    matrix = [[0] * i for i in range(256)] * 256
    if query == 'SetRow':
        for i in range(256):
            matrix[i][n] = x
    elif query == 'SetCol':
        for i in range(256):
            matrix[n][i] = x
    elif query == 'QueryRow':
        sumres = 0
        for i in range(256):
            sumres += matrix[n][i]
        return sumres
    elif query == 'QueryCol':
        sumres = 0
        for i in range(256):
            sumres += matrix[i][n]
        return sumres

# queryBoard('')