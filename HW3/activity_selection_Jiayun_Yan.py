def activity_selection(num,listoflist):
    listoflist.sort(key=lambda listoflist:listoflist[2])      #sort the list of events by finish time
    total = 0      #set the total to 0
    i = 0      #set index i to 0
    selected = []      #set the selected list as an empty one
    selected.append(i+1)      #the first activity is always selected, add it to the selected list
    total += 1      #increase total
    for j in range(num):      #the rest of the activities    
        if listoflist[j][1] >= listoflist[i][2]:      #if this activity has start time greater than or equal to the finish time of previously selected activity, then select it 
            selected.append(j+1)      #add it to the selected list
            total += 1      #increase total
            i = j      #set j as the last selected activity
    
    print("Number of activities selected = ", total)
    print("Activities: ", selected)

activity_selection(11,[[1,1,4],[2,3,5],[3,0,6],[4,5,7],[5,3,9],[6,5,9],[7,6,10],[8,8,11],[9,8,12],[10,2,14],[11,12,16]])