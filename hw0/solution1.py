# Задача 1. Малашенко Борис

def diagonalSum(mat):
    """
    :type mat: List[List[int]]
    """
    if len(mat) != len(mat[0]):
        return None

    sum = 0
    for i in range(len(mat)):
        ld = (i, i)
        rd = (i, len(mat) - i - 1)

        sum += mat[ld[0]][ld[1]]
        if ld != rd:
            sum += mat[rd[0]][rd[1]]

    return sum
