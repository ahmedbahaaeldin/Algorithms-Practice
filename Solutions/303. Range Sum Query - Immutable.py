class NumArray:

    def __init__(self, nums: List[int]):
        self.list = [0] * (len(nums)+1)
        if len(nums) > 0:
            for i,n in enumerate(nums):
                self.list[i+1] = self.list[i] + n

    def sumRange(self, i: int, j: int) -> int:
        return self.list[j+1] - self.list[i]
