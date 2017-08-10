def print_zigzag_matrix(matrix):
    direction = True
    for i in range(len(matrix)):
        if direction:
            flip = 0
        else:
            flip = len(matrix[i]) -1
        direction = not direction

        print('flip',flip)
        for j in range(len(matrix[i])):
            col = ( j + flip ) % len(matrix[i])
            print(str(matrix[i][col]),end=' ')
            if flip != 0:
                flip = flip -2
            print()



mat = [[1,2,3,4],
       [8,7,6,5],
       [9,10,11,12]

]

print_zigzag_matrix(mat)