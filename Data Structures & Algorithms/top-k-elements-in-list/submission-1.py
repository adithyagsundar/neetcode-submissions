class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        """
        bucket sort nums
        take the 
        """

        counts = [0] * 1000

        for i, num in enumerate(nums):
            counts[i] += 1 #counts of each num, 0 ... 1000


        i = 0
        #sort array based on frequency
        for n in counts:
            for j in range(counts[n] - 1):
                nums[i] = n
                i += 1
        
        return nums


        
