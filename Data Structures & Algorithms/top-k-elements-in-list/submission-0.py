class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        """
        bucket sort nums
        take the 
        """

        counts = [] * 1000

        for n, num in enumerate(nums):
            counts[n] += 1 #counts of each num, 0 ... 1000


        i = 0
        #sort array based on frequency
        for n in counts:
            for j in counts[n]:
                nums[i] = n
                i += 1
        


        
