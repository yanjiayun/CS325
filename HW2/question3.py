def binarysearch(target,matrix):
        rows=len(matrix)-1      #get index of rows
        cols=len(matrix[0])-1       #get index of cols
        i=0
        j=cols
        while i<=rows and j>=0:     #Start from the top right, move left or right based on value
            if target > matrix[i][j]:
                i += 1      #go down
            elif target < matrix[i][j]:
                j -= 1      #go left
            else:
                return (i,j)        #the target is found!
        return "Not Found"      #the target is not found!

def main():
    target = int(input("Please number need to be found in matrix: "))      #get user input of number need to be found in matrix
    m = int(input("Enter the number of rows:"))     #get user input of the number of rows
    n = int(input("Enter the number of columns:"))      #get user input of the number of columns
    matrix = []     # Initialize matrix 
    for i in range(m):          # A for loop for row entries 
        a =[] 
        for j in range(n):      # A for loop for column entries 
            a.append(int(input("Please enter the elements in matrix: ")))       #get user inputs of elements in matrix
        matrix.append(a)        #add user's inputs to the matrix
    print(binarysearch(target,matrix))      #run the function and print result

main()
    
"""print(binarysearch(10,[[2, 3, 4],[5, 7, 9],[11, 12, 13],[20, 22, 24]]))""" 