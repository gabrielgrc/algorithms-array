#Complexity Analysis : Time O(n) | Space O(1)
def moveZeroes(array):
    nonZeroIndex = 0
    
    for num in range(len(array)):
        if array[num] != 0:
            array[nonZeroIndex] = array[num]
            nonZeroIndex += 1
    
    for num in range(nonZeroIndex, len(array)):
        array[num] = 0
    
    return array
    
print(moveZeroes([1, 10, 0, 2, 8, 3, 0, 0, 6, 4, 0, 5, 7, 0]))
