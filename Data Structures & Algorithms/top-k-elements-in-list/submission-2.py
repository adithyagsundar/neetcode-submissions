class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        """
        bucket sort nums
        take the 
        """

        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1 #frequency map
        
        arr = []

        i = 0
        for num, freq in count.items():
            for j in range(freq - 1):
                arr[i] = num
                i += 1
        return arr

        
