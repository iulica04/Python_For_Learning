# Given a square matrix of characters write a script that prints the string obtained by going through the matrix in spiral order (as in the example):
# firs      1  2  3  4    =>   first_python_lab
# n_lt      12 13 14 5
# oba_      11 16 15 6
# htyp      10 9  8  7

def spiral_order(matrix) :
    top, bottom = 0, len(matrix)-1
    left, right = 0, len(matrix)-1

    result = ""


    while top <= bottom and left <= right :
        for i in range(left, right+1) :
            result = result + matrix[top][i]
        top += 1

        for i in range(top, bottom+1) :
            result += matrix[i][right]
        right -= 1

        for i in range(right, left-1, -1) :
            result += matrix[bottom][i]
        bottom -= 1

        for i in range(bottom, top-1, -1) :
            result += matrix[i][left]
        left += 1

    return result


if __name__ == "__main__" :
    # read the matrix
    n = int(input("Enter the size of the square matrix: "))

    matrix = []
    print(f"Enter the {n}x{n} matrix, row by row:")
    for _ in range(n):
        row = input().strip().split()
        if len(row) > n :
            print("Each row needs to have %d elements." % n)
            break
        matrix.append(row)


    print(spiral_order(matrix))

