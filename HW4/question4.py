def zombie_attack(matrix):
    zombie_positions = []      #create an array to stor the positions of zombies
    humans = 0      #initial the number of humans
    for i in range(len(matrix)):      #loop to find the zombies
        for j in range(len(matrix[0])):            
            if(matrix[i][j] == 2):      #if there is a zombies, add i,j to zombie_positions
                zombie_positions.append([i,j])            
            elif(matrix[i][j] == 1):      #if there is a preson, increse the number of humans
                humans = humans + 1
    if(humans == 0):      #if there are no human in the map, return 0
        return 0
    adjacency = [ [1,0],[-1,0],[0,1],[0,-1] ]      #position to add to get the 4 adjacent cells
    days = 0      #intial the number of days
    while(zombie_positions):      #keep doing the following code until zombie_positions become empty or break
        days += 1      #increse the number of days        
        for i in range(len(zombie_positions)):      #go through all the position of origin zombie        
            position = zombie_positions.pop(0)      #pop out the first position of origin zombile           
            for j in adjacency:      #go through all the possible adjacent cells               
                adj = [ position[0]+j[0] , position[1]+j[1] ]      #calculate the postion of adjacent cells              
                if(adj[0]>=0 and adj[0]<len(matrix) and adj[1]>=0 and adj[1]<len(matrix[0])):      #if adj position within matrix                
                    if(matrix[adj[0]][adj[1]] == 1):      #if there is a human
                        matrix[adj[0]][adj[1]] = 2      #change it to zombie              
                        humans -= 1      #decrese the number of humans 
                        if(humans == 0):      #if the number of human become to 0, then return the number of days
                            return days                        
                        zombie_positions.append(adj)      #append new zombie postion to zombie_positions                           
    return -1      #return -1 if its not possible that the whole group will become zombies

print(zombie_attack([ [ 1, 2, 1, 0, 0 ], [ 0, 0, 0, 0, 1], [ 2, 0, 0, 0, 2], [ 0, 0, 0, 0, 0] ] ) )
print(zombie_attack([ [ 1, 2, 1, 1, 0 ], [ 0, 0, 0, 0, 1], [ 2, 0, 0, 0, 2], [ 0, 0, 0, 1, 1] ] ) )