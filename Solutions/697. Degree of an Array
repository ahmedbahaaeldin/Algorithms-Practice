class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1
        if len(nums) == 2:
            if nums[0] == nums[1]:
                return 2
            else:
                return 1
        dp = {}
        visited = {}
        max_freq = {}
        for i,val in enumerate(nums):
            if val not in visited:
                visited[val] = i
                max_freq[val] = 1
            else:
                max_freq[val] += 1
                prev_index = visited[val]
                dp[val] = i-prev_index+1
        max_frequency_count = 0
        for k,v in max_freq.items():
            if v >= max_frequency_count:
                max_frequency_count = v
         
        if max_frequency_count == 1:
            return 1
        required_numbers = [k for k,v in max_freq.items() if v== max_frequency_count]
        
        min_route = []
        for r in required_numbers:
            min_route.append(dp[r])   
        return min(min_route)
