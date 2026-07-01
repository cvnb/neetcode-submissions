''' O(n^2) in the worst case
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            while l < r:
                if numbers[l] + numbers[r] == target:
                    return [l+1, r+1]
                r -= 1

            l += 1
            r = len(numbers) - 1
''' 

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            currSum = numbers[l] + numbers[r]
            if currSum == target:
                return [l+1, r+1]
            elif currSum < target:
                l += 1
            elif currSum > target:
                r -= 1