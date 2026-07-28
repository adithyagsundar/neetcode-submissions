class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
        create seen array
        iterate through list nums
        if value is not already in seen, add it to seen aray
        if it is in seen, return true
        """

        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
