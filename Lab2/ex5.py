# Write a function that receives as parameter a matrix and will return the matrix obtained by replacing
# all the elements under the main diagonal with 0 (zero).

# a00 a01 a02 a03
# a10 a11 a12 a13
# a20 a21 a22 a23
# a30 a31 a32 a33

def replacing(matrix, n) :
    new_matrix = matrix.copy()
    for i in range(0, n):
        for j in range(0, n):
            if i > j :
                new_matrix[i][j] = 0


    return matrix


if __name__ == "__main__" :
    n = int(input("Enter the size of the square matrix: "))

    matrix = []
    print(f"Enter the {n}x{n} matrix, row by row:")
    for _ in range(n):
        row = input().strip().split()
        if len(row) > n:
            print("Each row needs to have %d elements." % n)
            break
        matrix.append(row)

    print(replacing(matrix, n))