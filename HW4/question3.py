def count_islands(matrix):
    number = 0      #initial the number of islands
    if len(matrix) == 0:      #make sure the 2D matrix is not empty
        return number
    for i in range(len(matrix)):      #loop to get the number.
        for j in range(len(matrix[i])):
            if matrix[i][j] == 1:      #if there is the edge of island
                number = number + 1      #increase the number of islands
                DFS(matrix, i, j)      #use DFS function to find the whole island
    return number      #reutrn the number of islands

def DFS(matrix,rows,columns):
    row_length = len(matrix)      #initial the row length
    column_length = len(matrix[0])      #initial the column length 
    if rows < 0 or rows >= row_length or columns < 0 or columns >= column_length or matrix[rows][columns] == 0:      
    #when the index out the range of matrix or reaching water, stop DFS
        return 
    matrix[rows][columns] = 0      #After counting the area into island, make it into 0 to avoid endless loop
    DFS(matrix, rows + 1, columns)      #check the  right area
    DFS(matrix, rows - 1, columns)      #check the  left area
    DFS(matrix, rows, columns + 1)      #check the  bottom area
    DFS(matrix, rows, columns - 1)      #check the  top area

print(count_islands([[1,1,1,0,0],[0,0,0,0,1],[1,0,0,0,1],[0,0,0,0,0]]))