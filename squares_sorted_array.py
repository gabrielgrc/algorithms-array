class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        squared_array = [i ** 2 for i in nums]
        return sorted(squared_array)
