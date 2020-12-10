def insertsort(sort_list):
    for i in range(1, len(sort_list)): 
        key = sort_list[i] 
        j = i-1
        # Move elements of arr[0..i-1], that are greater than key, to one position ahead of their current position
        while j >= 0 and key < sort_list[j] : 
            sort_list[j + 1] = sort_list[j] 
            j -= 1
        sort_list[j + 1] = key 

def readFile(fileName):
    insertArrs = ''  # create a new string
    for line in open(fileName):
        num = line.split()   # ignore first number
        num_ = [int(x) for x in num[1:]] # convert x from string to int
        insertsort(num_) #sorting
        num_ = [str(x) for x in num_]  # convert x from int to string
        insertArrs += ' '.join(num_) + "\n" #Join all items in a tuple into a string, using a space character as separator
        
    f = open('insert.txt', 'w')     #Opens a file for writing, creates the file if it does not exist
    f.write(insertArrs) #write the insert sorted array
    f.close()

readFile('data.txt')