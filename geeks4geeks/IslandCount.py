def island_count(matrix):
    count = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == 1:
                count = count + 1
                print(row,col)
                mark(matrix,row,col)
                print(matrix)

    return count


def mark(matrix,row,col):
    if matrix[row][col] == 0:
        return
    else:
        matrix[row][col] = 0
        for i in range(row-1,row+2):
            for j in range(col-1,col+2):
                if i >= 0 and j >= 0 and i < len(matrix) and j < len(matrix[i]):
                    print('mark[',i,j,']')
                    mark(matrix,i,j)



mat = [[1, 1, 0, 0, 0],
       [0, 1, 0, 0, 1],
       [1, 0, 0, 1, 1],
       [0, 0, 0, 0, 0],
       [1, 0, 1, 0, 1] ]

print(island_count(mat))