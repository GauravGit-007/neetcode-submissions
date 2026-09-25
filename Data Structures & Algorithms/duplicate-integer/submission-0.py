class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        non_repeating=set()
        for i in nums:
            non_repeating.add(i)
        if len(nums)!=len(non_repeating):
            return True
        else:
            return False