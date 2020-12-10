from random import randint
import time

def insertsort(sort_list):
    for i in range(1, len(sort_list)): 
        key = sort_list[i] 
        j = i-1
        # Move elements of arr[0..i-1], that are greater than key, to one position ahead of their current position
        while j >= 0 and key < sort_list[j] : 
            sort_list[j + 1] = sort_list[j] 
            j -= 1
        sort_list[j + 1] = key 

def main():
    start = time.process_time()

    randomlist = []
    for i in range(0,23000):
        n = randint(0, 10000)
        randomlist.append(n)
    insertsort(randomlist)
    
    end = time.process_time()
    print("Processor time (in seconds):", end)  

main()