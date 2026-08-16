class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        prefix sum tells you the value of all the ints so far
        so if we want to take it from a non-prefix then we subtract the prefix sum right before it (i.e. subtracting everything before it which is not included)
        """

        res = []

        for i, num1 in enumerate(nums):
            product = 1
            for j, num2 in enumerate(nums):
                if i != j:
                    product = product * num2
            res.append(product)
        return res



            

