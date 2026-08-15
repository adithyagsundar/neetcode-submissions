class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        """
        take the count of each num , store in freq_map
        create a second arary where the INDEX is the frequency of the value and the values are stored in a list at that same index
        this is so we can iterate through the most frequent values (i.e. the largest index)
        """

        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1 #frequency map
        
        freq = [[] for i in range(len(nums) + 1)] #why nums + 1?

        for n, c in count.items():
            freq[c].append(n) #count (index) : number

        res = []

        for i in reversed(freq):
            for j in i:
                res.append(j)
                if len(res) == k:
                    return res


        

        

        
