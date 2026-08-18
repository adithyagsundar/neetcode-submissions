class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        if we multiply the prefix product by the postfix product at the same position, we will get the product of all nums except the num at that position 
        to save memory, we store both the prefix and postfix into the same res array
        """

        res = [0] * len(nums) #you must initialize the res array first with 0s to avoid index error

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix #become the current prefix
            prefix *= nums[i] #prefix multiplies itself by the current index BEFORE adding to the next iteration, so the number at that index always not included when added
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix #multiply instead of set because we already have the prefix values in there
            postfix *= nums[i] #postfix multipleis itself by the current index BEFORE adding to the next iteration
        return res



        

        




            

