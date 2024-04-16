class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # pseudocode
        # verify problem
        # keep a dictionary, key as the num in nums, value: number of times you see key
        counter_dict = dict()
        for num in nums:
            if num in counter_dict.keys():
                return True
            else:
                counter_dict[num] = 1
        return False
            
            
        
        