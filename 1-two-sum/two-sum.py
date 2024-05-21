class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted_nums = sorted(nums)
        i = 0
        # base case = 2 numbers
        length = len(nums)
        if length == 2:
            # assuming there's always one pair that satisfies the condition
            return [0, 1]
        for i in range(len(nums)):
            l = nums[i]
            rest = nums[i+1:]
            j = i+1
            for num in rest:
                if target == num + l:
                    return i, j
                j += 1