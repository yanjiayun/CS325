def partition(arr, l, r):      
    x = arr[r]      #It considers the last element as pivot 
    i = l 
    for j in range(l, r):          
        if arr[j] <= x:     #moves all smaller element to left of it and greater elements to right 
            arr[i], arr[j] = arr[j], arr[i]     #swap
            i += 1             
    arr[i], arr[r] = arr[r], arr[i]     #swap
    return i        #return index

def kthSmallest(arr, l, r, k): 
    if (k > 0 and k <= r - l + 1):      #if k is smaller than number of elements in array
        index = partition(arr, l, r)        #Partition the array around last element and get position of pivot element in sorted array 
        if (index - l == k - 1):        # if position is same as k 
            return arr[index] 
        if (index - l > k - 1):     # If position is more, recur for left subarray
            return kthSmallest(arr, l, index - 1, k)  
        return kthSmallest(arr, index + 1, r, k - index + l - 1)        # Else recur for right subarray
    return INT_MAX 

def quick_select(k,arr):
    l = 0       #start
    r = len(arr)-1      #end
    print("The kth smallest numebr is: ", kthSmallest(arr, l, r, k))        #print the result

def main():
    n = int(input("Please enter your array length: "))      #get user input of length of array
    k = int(input("Please enter the kth smallest number you want: "))       #get user input of k
    arr = []        #creat array
    for _ in range(0,n):
        ele = int(input("Please enter the elements in array: "))        #get user inputs of elements in array
        arr.append(ele)     #add user's inputs to the array
    quick_select(k,arr)     #run the quick select function

    """
    arr = []
    k = 
    quick_select(k,arr)
    """

main()