from functools import reduce
from operator import mul

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = []

        for i in range(0, len(nums)):
            a = nums.copy()
            a.pop(i)
            products.append(reduce(mul, a))

        return products


   