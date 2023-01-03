class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        
        doubleSet = set()
        
        for i in range(len(arr)):
            if arr[i] in doubleSet:
                return True
            doubleSet.add(arr[i] * 2)
            doubleSet.add(arr[i] / 2)
        return False
