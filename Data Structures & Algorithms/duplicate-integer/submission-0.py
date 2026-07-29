class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
        create seen array
        iterate through list nums
        if value is not already in seen, add it to seen aray
        if it is in seen, return true
        """

        seen = []

        for num in nums:
            if num not in seen:
                seen.append(num)
            else:
                return True
        return False
