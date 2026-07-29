class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:

        """
        appending each value in nums to ans twice
        O(n + n) since you do it twice
        can also just do return nums + nums, but this is better for interviews since you can easily change the amount of times you concatenate
        """
        ans = []
        
        for i in range(2):
            for num in nums:
                ans.append(num)
        return ans