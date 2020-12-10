from random import randint
import time

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

def main():
    start = time.process_time()

    randomlist = []
    for i in range(0,5):
        n = randint(0, 10000)
        randomlist.append(n)
    mergesort(randomlist)

    end = time.process_time()
    print("Processor time (in seconds):", end)  

main()