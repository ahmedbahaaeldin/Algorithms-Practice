class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if len(nums)==0:
            return 0
        mapping = {k:v for v,k in enumerate(nums)}
        def rec(target,list_of_numbers):
            left = list_of_numbers[:int(len(list_of_numbers)/2)]
            right = list_of_numbers[int(len(list_of_numbers)/2):]
            if target < min(left):
                result = mapping[left[0]] - 1
                return result
            elif target > max(right):
                result =  mapping[right[-1]] + 1
                return result
            elif target > max(left) and target < min(right):
                result = mapping[left[-1]] + 1
                return result
            elif target > min(left) and target < max(left):
                return rec(target,left)
            elif target > min(right) and target < max(right):
                return rec(target,right)
            
        if target in nums:
            return nums.index(target)
        elif target not in nums:
            if target > max(nums):
                return len(nums)
            elif target < min(nums):
                return 0
            elif target < max(nums) and target > min(nums):
                final = rec(target,nums)
                return final
