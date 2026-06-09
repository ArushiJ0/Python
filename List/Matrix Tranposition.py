def transpose(matrix):
        transpose_matrix = [[matrix[j][i] for j in range(len(matrix))] for i in range (len(matrix[0]))]
        return transpose_matrix

matrix = [[1,2,3] , [4,5,6], [7,8,9]]


for row in matrix:
     print(row)

transpose_matrix = transpose(matrix)
for row in transpose_matrix:
        print(row)
