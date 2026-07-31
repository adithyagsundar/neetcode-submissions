class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        create a hashmap for nums, with key being the index of the value and the value being the number
        difference = target - nums[i]
        iterare through the array, and if the difference exists in the hashmap, return those indices
        """

        hashmap = {}

        for i, num in enumerate(nums):
            hashmap[num] = i
        
        for i, num in enumerate(nums):
            diff = target - num
            if diff in hashmap and diff != i:
                return [i, hashmap[diff]]
