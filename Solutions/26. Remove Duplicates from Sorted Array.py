class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        flag = -100
        def remove_dup(nums):
            return list(set(nums))
        nums[:] = remove_dup(nums)
        nums.sort()
        return len(nums)
