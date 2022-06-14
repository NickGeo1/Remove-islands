''' THIS IS A CODING PROBLEM PROVIDED BY A Google Software Engineer DURING A GOOGLE INTERVIEW. 
THE PROBLEM IS REPRESENTED IN THE VIDEO https://www.youtube.com/watch?v=4tYoVx0QoN0.'''

#We refer to the length of columns as the size of the first row. We assume that each row has the same number of columns

def removeIslands(array_with_islands):

    array_without_islands = [[0 for col in range(len(array_with_islands[0]))] for row in range(len(array_with_islands))] #make an initial 0 array

    #Time complexity: O((n+m)*cost of findborderislands function) where n: rows, m:cols
    #Space complexity: O(n*m)
    for row in range(len(array_with_islands)): #for each row in array
        if(row == 0 or row == len(array_with_islands) - 1): #if we iterate first or last row
            #find islands starting from each column point at that row
            for col in range(len(array_with_islands[0])):
                array_without_islands = findBorderIslands(array_with_islands, array_without_islands, row, col)
        else: #if we iterate another row
            #find islands starting from first and last only column points at that row
            array_without_islands = findBorderIslands(array_with_islands, array_without_islands, row, 0)
            array_without_islands = findBorderIslands(array_with_islands, array_without_islands, row, len(array_with_islands[0]) - 1)

    return array_without_islands


def findBorderIslands(array_with_islands, current_array_without_islands, row, col):
    #if the current row,col has an 1 at the structuring new array, that means we already found this border island
    if(current_array_without_islands[row][col] == 1): 
        return current_array_without_islands

    #at this case the structuring new array dont have an 1 at row,col so we check if there is a border island at the array_with_islands 
    #to find and mark it to the structuring new array
    elif(array_with_islands[row][col] == 1):
        current_array_without_islands[row][col] = 1
        for direction in [(row + 1, col), (row, col - 1), (row - 1, col), (row, col + 1)]: #down, left, up, right directions
            #modify the structuring array by recursively checking neigbors digits. We check neighbors only if they are inside the bounds of the array
            if(direction[0] > -1 and direction[0] < len(array_with_islands) and direction[1] > -1 and direction[1] < len(array_with_islands[0])):
                current_array_without_islands = findBorderIslands(array_with_islands, current_array_without_islands, direction[0], direction[1])

    return current_array_without_islands

with_islands = [[1,1,0,1,1,1],
                [0,0,0,0,0,0],
                [0,0,1,1,1,1],
                [1,0,0,1,0,1],
                [1,0,1,0,0,0],
                [1,0,0,0,1,1]]

print("With islands:")
for row in with_islands:
    print(row)
print("\nWithout islands:")
for row in removeIslands(with_islands):
    print(row)