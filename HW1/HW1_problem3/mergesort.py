def mergesort(sort_list):
    if len(sort_list) > 1:
        mid = len(sort_list) // 2   # Finding the mid of the array 
        leftHalf = sort_list[:mid]  # Dividing the array elements into 2 halves
        rightHalf = sort_list[mid:] 
        mergesort(leftHalf)  # Sorting the first half 
        mergesort(rightHalf) # Sorting the second half 
        i = 0
        j = 0
        k = 0
        # Copy data to temp arrays leftHalf[] and rightHalf[] 
        while i < len(leftHalf) and j < len(rightHalf):
            if leftHalf[i] < rightHalf[j]:
                sort_list[k] = leftHalf[i]
                i = i + 1
            else:
                sort_list[k] = rightHalf[j]
                j = j + 1
            k = k + 1
        
        # Checking if any element was left 
        while i < len(leftHalf):
            sort_list[k] = leftHalf[i]
            i = i + 1
            k = k + 1
        while j < len(rightHalf):
            sort_list[k] = rightHalf[j]
            j = j + 1
            k = k + 1

def readFile(fileName):
    mergeArrs = '' # create a new string 
    for line in open(fileName):
        num = line.split()  # ignore first number
        num_ = [int(x) for x in num[1:]] # convert x from string to int
        mergesort(num_)     #sorting
        num_ = [str(x) for x in num_] # convert x from int to string
        mergeArrs += ' '.join(num_) + "\n" #Join all items in a tuple into a string, using a space character as separator

    f = open('merge.txt', 'w')     #Opens a file for writing, creates the file if it does not exist
    f.write(mergeArrs) #write the merge sorted array
    f.close()

readFile('data.txt')