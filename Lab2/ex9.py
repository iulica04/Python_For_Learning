# Write a function that receives as parameter a matrix which represents
# the heights of the spectators in a stadium and will return a list of tuples (line, column) each one representing
# a seat of a spectator which can't see the game. A spectator can't see the game if there is at least
# one taller spectator standing in front of him. All the seats are occupied. All the seats are at the same level.
# Row and column indexing starts from 0, beginning with the closest row from the field.
#
# 	Example:
#
# # FIELD
#
# [[1, 2, 3, 2, 1, 1],
#
# [2, 4, 4, 3, 7, 2],
#
# [5, 5, 2, 5, 6, 4],
#
# [6, 6, 7, 6, 7, 5]]
#
# Will return : [(2, 2), (3, 4), (2, 4)]

def disadvantaged_spectators(matrix):
    seats = list()
    n = len(matrix)
    m = len(matrix[0])

    while n > 1:
        for j in range(0, m):
            for i in range(n - 1, 0, -1):
                print(matrix[n - 1][j], matrix[i - 1][j])
                if matrix[n-1][j] <= matrix[i - 1][j]:
                    seat = (n-1, j)
                    seats.append(seat)
        print("\n\n\n\n")
        n -= 1

    return seats

if __name__ == "__main__" :
    matrix = [
        [1, 2, 3, 2, 1, 1],
        [2, 4, 4, 3, 7, 2],
        [5, 5, 2, 5, 6, 4],
        [6, 6, 7, 6, 7, 5]
    ]

    print(disadvantaged_spectators(matrix))