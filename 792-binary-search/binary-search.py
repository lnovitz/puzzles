class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # UMPIRE (understand, match, pseudocode, implement, review, evaluate)
        # set 3 pointers
        # left, middle, and right
        # middle is going to be the index equal to length of the array nums // 2 
        # [-1,0,3,5,9,12]
        # length = 6
        # l = 0, m = length // 2 = 3, r = length - 1 = 5
        # nums[l] = -1, nums[m] = 5, nums[r] = 12
        # target = 2, less than midpoint so update r = previous midpoint index = 3
        # l = 0, m = (previous midpoint) // 2 = 1, r = previous midpoint index = 3
        # nums[l] = -1, nums[m] = 0, nums[r] = 5
        # target = 2, more than midpoint, so update l = previous midpoint index = 1
        # l = (previous midpoint) = 1, m = (r // 2) = 1, r = 3
        # nums[l] = 0, nums[m] = 0, nums[r] = 5
        # condition, if r - l == 2, check target
        length = len(nums)
        l = 0
        r = length - 1      # 5
        m = (l + r) // 2     # 3

        while r - l > 2:
            if target < nums[m]:
                r = m
                m = (l + r) // 2
            elif target == nums[m]:
                return m
            else: # target > nums[m]
                l = m
                m = (l + r) // 2
        if target == nums[r]:
            return r
        if target == nums[l]:
            return l
        if target == nums[m]:
            return m
        return -1

            

        


        
        