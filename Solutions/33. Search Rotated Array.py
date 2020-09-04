class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums) -1
        while(i <= j):
            mid = (i+j)//2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                if target < nums[i] and nums[i] <= nums[mid]:
                    i = mid + 1
                else:
                    j = mid - 1
            elif target > nums[mid]:
                if target > nums[j] and nums[j] >= nums[mid]:
                    j = mid - 1
                else:
                    i = mid + 1
        return -1
                
